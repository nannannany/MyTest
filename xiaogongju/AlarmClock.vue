<template>
  <div class="alarm-app">
    <div class="alarm-container">
      <!-- 当前时间显示 -->
      <div class="time-display">{{ currentTime }}</div>

      <!-- 响铃时间 -->
      <div class="form-row">
        <div class="form-label">响铃时间</div>
        <div class="form-content">
      <!--时间选择器-->
          <el-config-provider :locale="zhCnCustom">
          <el-time-picker
              v-model="newAlarmTime"
              placeholder="响铃时间"
              format="HH:mm:ss"
              value-format="HH:mm:ss"
              style="width: 200px"
              size="default"
              :teleported="false"
          ></el-time-picker>
          </el-config-provider>
          <el-button size="small" style="width: 80px" @click="addAlarm" type="primary" plain>插入</el-button>
        </div>
      </div>

      <!-- 铃声选择 -->
      <div class="form-row">
        <div class="form-label">铃声选择</div>
        <div class="form-content">
          <el-select v-model="selectedRingtone" placeholder="选择铃声" style="width: 200px">
            <el-option v-for="item in ringtones" :key="item.value" :label="item.label" :value="item.value" />
          </el-select>
          <el-button size="small" style="width: 80px" @click="previewRingtone" type="success" plain>试听</el-button>
        </div>
      </div>

      <!-- 响铃时长 -->
      <div class="form-row">
        <div class="form-label">响铃时长</div>
        <div class="form-content">
          <el-select v-model="ringDuration" placeholder="响铃时长" style="width: 120px">
            <el-option label="5秒" :value="5" />
            <el-option label="10秒" :value="10" />
            <el-option label="30秒" :value="30" />
            <el-option label="60秒" :value="60" />
          </el-select>
        </div>
      </div>

      <!-- 整点报时 -->
      <div class="form-row">
        <div class="form-label">整点报时</div>
        <div class="form-content">
          <el-switch v-model="hourlyChime" />
        </div>
      </div>

      <!-- 闹钟列表表格展示 -->
      <div class="form-row">
        <div class="form-label">闹钟列表</div>
        <div class="form-content">
          <el-table :data="alarms" border style="width: 100%">
            <el-table-column prop="time" label="时间" width="120" />
            <el-table-column label="状态" width="80">
              <template #default="{ row }">
                <el-switch v-model="row.enabled" @change="saveAlarms" />
              </template>
            </el-table-column>
            <el-table-column label="操作" width="100">
              <template #default="{ $index }">
                <el-button type="danger" size="small" style="width: 60px" @click="deleteAlarm($index)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </div>

      <!-- 响铃模态框 -->
      <el-dialog v-model="ringing" title="响铃提醒" :close-on-click-modal="false" width="30%">
        <p>时间到了：{{ ringingTime }}</p>
        <template #footer>
          <el-button size="small" style="width: 80px" @click="stopRingtone">关闭</el-button>
        </template>
      </el-dialog>

      <!-- 隐藏音频元素，用于播放 -->
      <audio ref="audio" preload="auto"></audio>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import zhCn from 'element-plus/es/locale/lang/zh-cn'

// 局部覆盖按钮文本
const zhCnCustom = {
  ...zhCn,
  el: {
    ...zhCn.el,
    datepicker: {
      ...zhCn.el.datepicker,
      cancel: '取消',
      confirm: '确认',
    },
  },
}

// 响铃列表时间
const currentTime = ref('')
const newAlarmTime = ref('')
const selectedRingtone = ref('default')
const ringDuration = ref(10)
const hourlyChime = ref(false)
const alarms = ref([])
const ringing = ref(false)
const ringingTime = ref('')
const audio = ref(null)

// 可选铃声列表，对应 public/ringtones 下的文件名
const ringtones = [
  { label: '默认铃声', value: 'default' },
  { label: '清晨鸟鸣', value: 'birds' },
  { label: '电子哔哔', value: 'beep' },
  { label: '温柔钢琴', value: 'piano' },
]

// 更新当前时分秒
function updateCurrentTime() {
  const now = new Date()
  currentTime.value = now.toTimeString().slice(0, 8)
}

// 添加闹钟
function addAlarm() {
  if (!newAlarmTime.value) return
  alarms.value.push({ time: newAlarmTime.value, enabled: true })
  saveAlarms()
  newAlarmTime.value = ''
}

// 删除闹钟
function deleteAlarm(index) {
  alarms.value.splice(index, 1)
  saveAlarms()
}

// 播放铃声
function playRingtone() {
  const srcMap = {
    default: '/ringtones/default.mp3',
    birds: '/ringtones/birds.mp3',
    beep: '/ringtones/beep.mp3',
    piano: '/ringtones/piano.mp3',
  }
  const src = srcMap[selectedRingtone.value] || srcMap.default
  if (audio.value) {
    audio.value.src = src
    audio.value.play().catch(() => {})
  }
}

// 停止铃声
function stopRingtone() {
  if (audio.value) {
    audio.value.pause()
    audio.value.currentTime = 0
  }
  ringing.value = false
}

// 试听
function previewRingtone() {
  playRingtone()
  setTimeout(() => {
    stopRingtone()
  }, 3000)
}

// 检查闹钟触发
function checkAlarms() {
  const now = new Date()
  const timeStr = now.toTimeString().slice(0, 8)
  alarms.value.forEach(alarm => {
    if (alarm.enabled && alarm.time === timeStr) {
      triggerAlarm(timeStr)
    }
  })
  // 整点报时：分钟秒都为0
  if (hourlyChime.value && now.getMinutes() === 0 && now.getSeconds() === 0) {
    triggerAlarm(timeStr)
  }
}

// 触发响铃
function triggerAlarm(time) {
  if (ringing.value) return
  ringingTime.value = time
  ringing.value = true
  playRingtone()
  setTimeout(() => {
    stopRingtone()
  }, ringDuration.value * 1000)
}

// 本地存储闹钟与设置
function saveAlarms() {
  localStorage.setItem('alarms', JSON.stringify(alarms.value))
  localStorage.setItem('ringDuration', String(ringDuration.value))
  localStorage.setItem('hourlyChime', String(hourlyChime.value))
  localStorage.setItem('selectedRingtone', selectedRingtone.value)
}

function loadAlarms() {
  const stored = localStorage.getItem('alarms')
  if (stored) {
    try {
      alarms.value = JSON.parse(stored)
    } catch {}
  }
  const rd = parseInt(localStorage.getItem('ringDuration'))
  if (!isNaN(rd)) ringDuration.value = rd
  const hc = localStorage.getItem('hourlyChime')
  if (hc === 'true') hourlyChime.value = true
  const sr = localStorage.getItem('selectedRingtone')
  if (sr) selectedRingtone.value = sr
}

// 初始化
onMounted(() => {
  audio.value = document.querySelector('audio')
  loadAlarms()
  updateCurrentTime()
  setInterval(updateCurrentTime, 1000)
  setInterval(checkAlarms, 1000)
})
</script>

<style scoped>
.alarm-container {
  font-family: Arial, sans-serif;
  max-width: 550px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.time-display {
  font-size: 48px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
}

.form-row {
  display: flex;
  align-items: center;
  width: 100%;
  margin-bottom: 10px;
}

.form-label {
  width: 80px;
  font-weight: bold;
}

.form-content {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1;
}

</style>