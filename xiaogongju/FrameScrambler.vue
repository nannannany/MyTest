<template>
  <el-card class="frame-scrambler-card">
      <h1>遥测帧加/解扰工具</h1>
      <br>

    <el-form :model="form" label-width="100px" class="form-container">
      <!-- 扰码输入 -->
      <el-form-item label="扰码 (Hex)">
        <el-input
            v-model="form.scrambleHex"
            placeholder="4位十六进制，例如 09D7"
            maxlength="4"
            @input="onScrambleHexInput"
            clearable
            style="width: 150px;"
        />
        <div v-if="scrambleCodeError" class="error-text">{{ scrambleCodeError }}</div>
      </el-form-item>

      <!-- 上传文件 -->
      <el-form-item label="上传数据帧">
        <el-upload
            class="upload-demo"
            :before-upload="beforeUpload"
            :show-file-list="false"
            accept=".bin,.dat"
        >
          <el-button type="primary" plain>选择文件</el-button>
        </el-upload>
        <div v-if="fileName" class="file-info">
          已选择：<strong>{{ fileName }}</strong>
        </div>
      </el-form-item>

      <!-- 操作按钮 -->
      <el-form-item label="操作">
        <div class="button-group">
          <el-button type="primary" :disabled="!canOperate" @click="manualScramble" plain>加扰</el-button>
          <el-button type="warning" :disabled="!canOperate" @click="manualDescramble" plain>解扰</el-button>
          <el-button type="danger" :disabled="!hasProcessed" @click="handleReset" plain>重置</el-button>
          <el-button type="success" :disabled="!hasProcessed" @click="download" plain>导出结果</el-button>
        </div>
      </el-form-item>
    </el-form>

    <!-- 预览区域 -->
    <div v-if="hexPreview" class="preview-container">
      <div class="preview-header"><strong>十六进制预览（前 256 字节示例，可滚动查看全部）：</strong></div>
      <pre class="hex-preview">{{ hexPreview }}</pre>
    </div>
  </el-card>
</template>

<script setup>
import { ref, reactive, computed, watch } from 'vue'
import { ElMessage } from 'element-plus'

const props = defineProps({
  defaultScrambleCode: { type: String, default: '09D7' },
  action: { type: String, default: '' },         // 'scramble' | 'descramble' | 'reset' | ''
  actionTrigger: { type: Number, default: 0 }
})
const emit = defineEmits(['processed', 'reseted', 'error'])

// 表单状态
const form = reactive({
  scrambleHex: props.defaultScrambleCode.toUpperCase()
})

// 原始与当前处理后数据
const originalBytes = ref(null)
const currentBytes = ref(null)
const fileName = ref('')

// 预览十六进制
const hexPreview = ref('')

// 扰码校验
const scrambleCodeError = ref('')
function onScrambleHexInput(val) {
  form.scrambleHex = val.toUpperCase().replace(/[^0-9A-F]/g, '')
  if (form.scrambleHex.length > 4) {
    form.scrambleHex = form.scrambleHex.slice(0, 4)
  }
  if (!/^[0-9A-F]{1,4}$/.test(form.scrambleHex)) {
    scrambleCodeError.value = '请输入1~4位十六进制字符'
  } else {
    scrambleCodeError.value = ''
  }
}

// 上传前校验并读取
async function beforeUpload(file) {
  // file: JS File 对象，无类型注解
  try {
    const buffer = await file.arrayBuffer()
    const bytes = new Uint8Array(buffer)
    if (bytes.length !== 1024) {
      ElMessage.error('上传失败：文件长度必须为 1024 字节')
      emit('error', '文件长度必须为 1024 字节')
      return false
    }
    originalBytes.value = new Uint8Array(bytes)
    currentBytes.value = new Uint8Array(bytes)
    fileName.value = file.name
    updateHexPreview(currentBytes.value)
    ElMessage.success('文件加载成功，长度 1024 字节')
  } catch (err) {
    console.error(err)
    ElMessage.error('读取文件时出错')
    emit('error', '读取文件时出错')
  }
  return false
}

const canOperate = computed(() => {
  return currentBytes.value !== null && !scrambleCodeError.value && form.scrambleHex.length > 0
})
const hasProcessed = computed(() => {
  return originalBytes.value !== null
      && currentBytes.value !== null
      && !arraysEqual(originalBytes.value, currentBytes.value)
})

// 更新预览
function updateHexPreview(bytes) {
  const len = bytes.length
  const maxShow = 256
  const showLen = Math.min(len, maxShow)
  const lines = []
  for (let offset = 0; offset < showLen; offset += 16) {
    const slice = bytes.slice(offset, Math.min(offset + 16, showLen))
    const hexs = Array.from(slice).map(b => b.toString(16).padStart(2, '0')).join(' ')
    lines.push(hexs)
  }
  let preview = lines.join('\n')
  if (len > maxShow) {
    preview += `\n... 共 ${len} 字节，总览前 ${maxShow} 字节`
  }
  hexPreview.value = preview
}
function arraysEqual(a, b) {
  if (a === b) return true
  if (!a || !b) return false
  if (a.length !== b.length) return false
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) return false
  }
  return true
}

// 异或处理
function scrambleXOR(bytes, codeHex) {
  const code = parseInt(codeHex, 16)
  const high = (code >> 8) & 0xFF
  const low = code & 0xFF
  const buf = new Uint8Array(bytes)
  for (let i = 27; i <= 1021; i++) {
    const use = ((i - 27) % 2 === 0 ? high : low)
    buf[i] = buf[i] ^ use
  }
  return buf
}

// 手动操作
function manualScramble() {
  if (!canOperate.value) return
  try {
    const out = scrambleXOR(currentBytes.value, form.scrambleHex)
    currentBytes.value = out
    updateHexPreview(out)
    ElMessage.success('已执行加扰操作')
    emit('processed', out)
  } catch (err) {
    console.error(err)
    ElMessage.error('加扰时出错')
    emit('error', '加扰时出错')
  }
}
function manualDescramble() {
  if (!canOperate.value) return
  try {
    const out = scrambleXOR(currentBytes.value, form.scrambleHex)
    currentBytes.value = out
    updateHexPreview(out)
    ElMessage.success('已执行解扰操作')
    emit('processed', out)
  } catch (err) {
    console.error(err)
    ElMessage.error('解扰时出错')
    emit('error', '解扰时出错')
  }
}
function handleReset() {
  if (!originalBytes.value) return
  currentBytes.value = new Uint8Array(originalBytes.value)
  updateHexPreview(currentBytes.value)
  ElMessage.info('已重置为原始数据')
  emit('reseted', currentBytes.value)
}
function download() {
  if (!currentBytes.value) return
  const blob = new Blob([currentBytes.value], { type: 'application/octet-stream' })
  const url = URL.createObjectURL(blob)
  const name = fileName.value ? `processed_${fileName.value}` : 'processed_frame.bin'
  const a = document.createElement('a')
  a.href = url
  a.download = name
  a.click()
  URL.revokeObjectURL(url)
  ElMessage.success(`已下载：${name}`)
}

// 外部 Props 触发操作
let lastTrigger = props.actionTrigger
watch(
    () => props.actionTrigger,
    (newVal) => {
      if (newVal !== lastTrigger) {
        lastTrigger = newVal
        if (!originalBytes.value) {
          ElMessage.warning('尚未上传文件，无法执行外部操作')
          emit('error', '尚未上传文件')
          return
        }
        if (scrambleCodeError.value) {
          ElMessage.warning('扰码格式不正确，无法执行外部操作')
          emit('error', '扰码格式不正确')
          return
        }
        if (props.action === 'scramble') {
          try {
            const out = scrambleXOR(currentBytes.value, form.scrambleHex)
            currentBytes.value = out
            updateHexPreview(out)
            ElMessage.success('外部触发：已执行加扰')
            emit('processed', out)
          } catch (err) {
            console.error(err)
            ElMessage.error('外部触发加扰时出错')
            emit('error', '外部触发加扰时出错')
          }
        } else if (props.action === 'descramble') {
          try {
            const out = scrambleXOR(currentBytes.value, form.scrambleHex)
            currentBytes.value = out
            updateHexPreview(out)
            ElMessage.success('外部触发：已执行解扰')
            emit('processed', out)
          } catch (err) {
            console.error(err)
            ElMessage.error('外部触发解扰时出错')
            emit('error', '外部触发解扰时出错')
          }
        } else if (props.action === 'reset') {
          handleReset()
        } else {
        }
      }
    }
)
</script>

<style scoped>
.frame-scrambler-card {
  font-family: Arial, sans-serif;
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
.preview-container {
  margin-top: 20px;
}
.preview-header {
  margin-bottom: 6px;
}
.hex-preview {
  background: #1e1e1e;
  color: #d4d4d4;
  padding: 10px;
  border-radius: 4px;
  overflow-x: auto;
  font-family: 'Courier New', monospace;
  font-size: 13px;
  max-height: 300px;
}
.error-text {
  color: #f56c6c;
  font-size: 12px;
  margin-top: 4px;
}
.file-info {
  margin-top: 6px;
  font-size: 14px;
}
</style>
