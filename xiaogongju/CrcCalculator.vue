<template>
  <div class="crc-calculator">
    <h1>
      CRC（循环冗余校验）在线计算
    </h1>
    <br>

    <!-- ----- 输入选项 ----- -->
    <div class="separator">----- 输入选项 -----</div>
    <div class="section input-options">
      <!-- 输入类型单选 -->
      <div class="input-group row">
        <label class="input-label">输入类型</label>
        <div class="radio-group-inline">
          <label class="radio-label-inline">
            <input
                type="radio"
                :checked="inputType === 'hex'"
                @change="handleInputTypeChange('hex')"
                class="radio-input"
            />
            Hex
          </label>
          <label class="radio-label-inline">
            <input
                type="radio"
                :checked="inputType === 'ascii'"
                @change="handleInputTypeChange('ascii')"
                class="radio-input"
            />
            ASCII
          </label>
        </div>
      </div>

      <!-- 需要校验的数据 -->
      <div class="input-group column">
        <label class="input-label">需要校验的数据</label>
        <textarea
            v-model="inputData"
            :disabled="isFileMode"
            :placeholder="inputType === 'hex' ? '例如: 31 32 33 34' : '例如: 1234'"
            class="data-textarea"
            :class="{ 'disabled': isFileMode }"
        />
      </div>

      <!-- 文件上传按钮 -->
      <div class="input-group row">
        <label class="input-label">文件输入</label>
        <input
            type="file"
            ref="fileInputRef"
            @change="handleFileUpload"
            style="display: none"
        />
        <el-button
            @click="$refs.fileInputRef.click()"
            class="file-button nowrap"
            type="primary"
            plain
        >
          {{ isFileMode ? '更换文件' : '插入文件' }}
        </el-button>
      </div>
    </div>

    <!-- ----- 参数设置 ----- -->
    <div class="separator">----- 参数设置 -----</div>
    <div class="section param-settings">
      <div class="input-group row">
        <label class="input-label">参数模型 NAME</label>
        <select
            v-model="selectedModel"
            @change="handleModelChange"
            class="model-select nowrap"
        >
          <option value="CRC-16/CCITT-FALSE">CRC-16/CCITT-FALSE</option>
          <option value="自定义">自定义</option>
        </select>
      </div>

      <!-- 宽度 WIDTH -->
      <div class="input-group row">
        <label class="input-label nowrap">宽度 WIDTH</label>
        <input
            type="text"
            v-model="width"
            class="param-input nowrap"
            :disabled="selectedModel !== '自定义'"
        />
      </div>

      <!-- 多项式 POLY -->
      <div class="input-group row">
        <label class="input-label nowrap">多项式 POLY (Hex)</label>
        <input
            type="text"
            v-model="poly"
            class="param-input nowrap"
            :disabled="selectedModel !== '自定义'"
        />
      </div>

      <!-- 初始值 INIT -->
      <div class="input-group row">
        <label class="input-label nowrap">初始值 INIT (Hex)</label>
        <input
            type="text"
            v-model="init"
            class="param-input nowrap"
            :disabled="selectedModel !== '自定义'"
        />
      </div>

      <!-- 结果异或值 XOROUT -->
      <div class="input-group row">
        <label class="input-label nowrap">结果异或值(Hex)</label>
        <input
            type="text"
            v-model="xorout"
            class="param-input nowrap"
            :disabled="selectedModel !== '自定义'"
        />
      </div>

      <!-- 反转选项复选框 -->
      <div class="input-group row">
        <label class="input-label nowrap">反转选项</label>
        <div class="checkbox-group-inline">
          <label class="checkbox-label-inline nowrap">
            <input
                type="checkbox"
                v-model="refin"
                class="checkbox-input"
                :disabled="selectedModel !== '自定义'"
            />
            输入数据反转 (REFIN)
          </label>
          <label class="checkbox-label-inline nowrap">
            <input
                type="checkbox"
                v-model="refout"
                class="checkbox-input"
                :disabled="selectedModel !== '自定义'"
            />
            输出数据反转 (REFOUT)
          </label>
        </div>
      </div>
    </div>

    <!-- ----- 操作按钮 ----- -->
    <div class="input-group row">
      <label class="input-label nowrap">操作</label>
      <div class="result-button-group-inline">
        <el-button @click="calculateCRC" class="action-button nowrap" type="primary" plain>计算</el-button>
        <el-button @click="clearAll" class="action-button nowrap" type="danger" plain>清空</el-button>
      </div>
    </div>

    <!-- ----- 结果显示 ----- -->
    <div class="separator">----- 结果显示 -----</div>
    <div class="section result-display">
      <!-- 提示信息 -->
      <div class="warning-text">
        高位在左低位在右，使用时请注意高低位顺序！！！
      </div>
      <br>
      <div class="input-group row">
        <label class="input-label nowrap">校验计算结果 (Hex)</label>
        <input
            type="text"
            :value="resultHex"
            readonly
            class="result-input nowrap"
        />
      </div>
      <div class="input-group row">
        <label class="input-label nowrap">校验计算结果 (Bin)</label>
        <input
            type="text"
            :value="resultBin"
            readonly
            class="result-input nowrap"
        />
      </div>
      <div class="input-group row">
        <label class="input-label nowrap">操作</label>
        <div class="result-button-group-inline">
          <el-button
              @click="copyResult"
              :disabled="!resultHex"
              class="result-button nowrap"
              :class="{ 'disabled': !resultHex }"
              type="primary"
              plain
          >复制
          </el-button>
          <el-button
              @click="exportResult"
              :disabled="!resultHex"
              class="result-button export-button nowrap"
              :class="{ 'disabled': !resultHex }"
              type="warning"
              plain
          >导出文件
          </el-button>
        </div>
      </div>
    </div>



    <div v-if="showSwitchModal" class="modal-overlay" @click.self="">
      <div class="modal-content">
        <h4 class="modal-title">数据处理选择</h4>
        <p class="modal-text">
          检测到输入框中有数据，请选择如何处理：
        </p>
        <div class="modal-button-group">
          <button @click="handleSwitchConfirm('convert')" class="modal-button convert nowrap">
            转换数据
          </button>
          <button @click="handleSwitchConfirm('clear')" class="modal-button clear nowrap">
            清除数据
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'

const inputType = ref('hex')
const inputData = ref('')
const selectedModel = ref('CRC-16/CCITT-FALSE')
const width = ref('16')
const poly = ref('1021')
const init = ref('FFFF')
const xorout = ref('0000')
const refin = ref(false)
const refout = ref(false)
const resultHex = ref('')
const resultBin = ref('')
const showSwitchModal = ref(false)
const pendingInputType = ref('')
const isFileMode = ref(false)
const fileInputRef = ref(null)

const crcModels = {
  'CRC-16/CCITT-FALSE': {
    width: '16',
    poly: '1021',
    init: 'FFFF',
    xorout: '0000',
    refin: false,
    refout: false
  }
}

const handleInputTypeChange = (newType) => {
  if (inputData.value.trim() !== '') {
    pendingInputType.value = newType
    showSwitchModal.value = true
  } else {
    inputType.value = newType
  }
}

const handleSwitchConfirm = (action) => {
  if (action === 'convert') {
    if (pendingInputType.value === 'ascii' && inputType.value === 'hex') {
      const hexData = inputData.value.replace(/\s+/g, '')
      let asciiData = ''
      for (let i = 0; i < hexData.length; i += 2) {
        const hex = hexData.substr(i, 2)
        if (hex.length === 2) {
          asciiData += String.fromCharCode(parseInt(hex, 16))
        }
      }
      inputData.value = asciiData
    } else if (pendingInputType.value === 'hex' && inputType.value === 'ascii') {
      // Convert ascii to hex
      let hexData = ''
      for (let i = 0; i < inputData.value.length; i++) {
        hexData += inputData.value.charCodeAt(i).toString(16).toUpperCase().padStart(2, '0') + ' '
      }
      inputData.value = hexData.trim()
    }
  } else if (action === 'clear') {
    inputData.value = ''
  }
  inputType.value = pendingInputType.value
  showSwitchModal.value = false
  isFileMode.value = false
}

const handleModelChange = () => {
  if (selectedModel.value === 'CRC-16/CCITT-FALSE') {
    const modelData = crcModels[selectedModel.value]
    width.value = modelData.width
    poly.value = modelData.poly
    init.value = modelData.init
    xorout.value = modelData.xorout
    refin.value = modelData.refin
    refout.value = modelData.refout
  } else {
    width.value = ''
    poly.value = ''
    init.value = ''
    xorout.value = ''
    refin.value = false
    refout.value = false
  }
}

const handleFileUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      const content = e.target.result
      if (inputType.value === 'hex') {
        // Convert file content to hex
        let hexData = ''
        for (let i = 0; i < content.length; i++) {
          hexData += content.charCodeAt(i).toString(16).toUpperCase().padStart(2, '0') + ' '
        }
        inputData.value = hexData.trim()
      } else {
        inputData.value = content
      }
      isFileMode.value = true
    }
    reader.readAsText(file)
  }
}

const reverseBits = (value, bits) => {
  let result = 0
  for (let i = 0; i < bits; i++) {
    result = (result << 1) | ((value >> i) & 1)
  }
  return result
}

const calculateCRC = () => {
  if (!inputData.value.trim() || !width.value || !poly.value || init.value === '' || xorout.value === '') {
    alert('请填写完整的参数')
    return
  }

  try {
    const widthNum = parseInt(width.value)
    const polyNum = parseInt(poly.value, 16)
    const initNum = parseInt(init.value, 16)
    const xoroutNum = parseInt(xorout.value, 16)

    let data = []
    if (inputType.value === 'hex') {
      const hexData = inputData.value.replace(/\s+/g, '')
      for (let i = 0; i < hexData.length; i += 2) {
        const hex = hexData.substr(i, 2)
        if (hex.length === 2) {
          data.push(parseInt(hex, 16))
        }
      }
    } else {
      for (let i = 0; i < inputData.value.length; i++) {
        data.push(inputData.value.charCodeAt(i))
      }
    }

    let crc = initNum
    const topBit = 1 << (widthNum - 1)
    const mask = (1 << widthNum) - 1

    for (let byte of data) {
      if (refin.value) {
        byte = reverseBits(byte, 8)
      }

      crc ^= (byte << (widthNum - 8))

      for (let bit = 0; bit < 8; bit++) {
        if (crc & topBit) {
          crc = (crc << 1) ^ polyNum
        } else {
          crc = crc << 1
        }
        crc &= mask
      }
    }

    if (refout.value) {
      crc = reverseBits(crc, widthNum)
    }

    crc ^= xoroutNum
    crc &= mask

    const hexResult = crc.toString(16).toUpperCase().padStart(Math.ceil(widthNum / 4), '0')
    const binResult = crc.toString(2).padStart(widthNum, '0')

    resultHex.value = hexResult
    resultBin.value = binResult

  } catch (error) {
    alert('计算错误，请检查输入参数')
  }
}

const clearAll = () => {
  inputData.value = ''
  resultHex.value = ''
  resultBin.value = ''
  isFileMode.value = false
  if (fileInputRef.value) {
    fileInputRef.value.value = ''
  }
}

const copyResult = () => {
  navigator.clipboard.writeText(resultHex.value)
  alert('结果已复制到剪贴板')
}

const exportResult = () => {
  const result = `CRC计算结果\n十六进制: ${resultHex.value}\n二进制: ${resultBin.value}`
  const blob = new Blob([result], {type: 'text/plain'})
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'crc_result.txt'
  a.click()
  URL.revokeObjectURL(url)
}
</script>

<style scoped>
.crc-calculator {
  font-family: Arial, sans-serif;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.separator {
  text-align: center;
  font-family: monospace;
  color: #495057;
  position: relative;
}

.section {
  margin-bottom: 20px;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.input-group.row {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.input-group.row .input-label {
  margin-right: 10px;
  width: 150px;
  font-size: 14px;
  color: #495057;
  text-align: left;
  white-space: nowrap;
  flex-shrink: 0;
}

.input-group.row > *:not(.input-label) {
  flex: 1;
  min-width: 0;
}

.input-group.column {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
}

.input-group.column .input-label {
  margin-bottom: 8px;
  font-size: 14px;
  color: #495057;
  text-align: left;
}

.nowrap {
  white-space: nowrap;
}

.radio-group-inline {
  display: flex;
  gap: 20px;
}

.radio-label-inline {
  font-size: 14px;
  display: flex;
  align-items: center;
  white-space: nowrap;
}

.radio-input {
  margin-right: 6px;
}

.checkbox-group-inline {
  display: flex;
  gap: 20px;
}

.checkbox-label-inline {
  font-size: 14px;
  display: flex;
  align-items: center;
  white-space: nowrap;
}

.checkbox-input {
  margin-right: 6px;
}

.data-textarea {
  width: 100%;
  min-height: 100px;
  padding: 8px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  font-size: 14px;
  background-color: #fff;
  resize: vertical;
  box-sizing: border-box;
}

.data-textarea.disabled {
  background-color: #f8f9fa;
}


.model-select {
  padding: 6px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  font-size: 14px;
  width: 100%;
  box-sizing: border-box;
}

.model-select.nowrap {
  white-space: nowrap;
}

.param-input {
  padding: 6px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  font-size: 14px;
  box-sizing: border-box;
}

.param-input:disabled {
  background-color: #e9ecef;
  cursor: not-allowed;
}

.param-input.nowrap {
  white-space: nowrap;
}

.result-input {
  padding: 6px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  font-size: 14px;
  background-color: #f8f9fa;
  box-sizing: border-box;
}

.result-input.nowrap {
  white-space: nowrap;
}

.warning-text {
  color: #dc3545;
  font-size: 14px;
  font-weight: 500;
  text-align: left;
  margin-top: 10px;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  padding: 30px;
  border-radius: 8px;
  min-width: 300px;
  text-align: center;
}

.modal-title {
  margin-bottom: 20px;
  color: #495057;
}

.modal-text {
  margin-bottom: 25px;
  color: #6c757d;
}

</style>
