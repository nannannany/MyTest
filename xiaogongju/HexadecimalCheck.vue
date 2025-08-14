<template>
  <div class="calculator-container">
    <h1>ASCII/HEX 校验和计算器</h1>
    <br>
    <table class="checksum-table">
      <tbody>
      <tr>
        <th>10进制求和</th>
        <td>{{ sumDec || '' }}</td>
      </tr>
      <tr>
        <th>16进制求和</th>
        <td>{{ sumHex || '' }}</td>
      </tr>
      <tr>
        <th>校验一（2字节,HEX）</th>
        <td>{{ crc16 || '' }}</td>
      </tr>
      <tr>
        <th>校验二（2字节,HEX）</th>
        <td>{{ checksum || '' }}</td>
      </tr>
      <tr>
        <th>字节数(HEX)</th>
        <td>{{ byteLengthHex || '' }}</td>
      </tr>
      </tbody>
    </table>




    <textarea
        v-model="inputText"
        rows="8"
        placeholder="请输入内容"
    ></textarea>

    <div class="button-row">
      <select v-model="inputMode">
        <option value="ascii">ASCII</option>
        <option value="hex">HEX</option>
      </select>
      <span></span>
      <span></span>
      <el-button @click="calculate" type="primary" plain>计算</el-button>
      <el-button @click="clear" type="danger" plain>清除</el-button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// 引入 Element Plus
import { ElButton } from 'element-plus'
import 'element-plus/dist/index.css'

// 输入模式
const inputMode = ref('ascii')
const inputText = ref('')

// 输出值
const sumDec = ref('')
const sumHex = ref('')
const crc16 = ref('')
const checksum = ref('')
const byteLengthHex = ref('')

// 计算函数
function calculate() {
  let bytes = []
  try {
    if (inputMode.value === 'ascii') {
      bytes = [...inputText.value].map(char => char.charCodeAt(0))
    } else {
      const hexClean = inputText.value.replace(/[^0-9a-fA-F]/g, '')
      if (hexClean.length % 2 !== 0) throw new Error('HEX 输入位数应为偶数')
      for (let i = 0; i < hexClean.length; i += 2) {
        bytes.push(parseInt(hexClean.slice(i, i + 2), 16))
      }
    }
  } catch (e) {
    alert('输入错误：' + e.message)
    return
  }

  // 求和
  const decSum = bytes.reduce((acc, b) => acc + b, 0)
  sumDec.value = decSum.toString()
  sumHex.value = decSum.toString(16).toUpperCase().padStart(4, '0')

  // CRC16 校验（Modbus CRC16）
  crc16.value = computeCRC16(bytes)

  // 简单累加校验（低16位）
  const low16 = decSum & 0xFFFF
  checksum.value = low16.toString(16).toUpperCase().padStart(4, '0')

  byteLengthHex.value = bytes.length.toString(16).toUpperCase().padStart(2, '0')
}

function clear() {
  inputText.value = ''
  sumDec.value = ''
  sumHex.value = ''
  crc16.value = ''
  checksum.value = ''
  byteLengthHex.value = ''
}

// CRC16/MODBUS算法
function computeCRC16(data) {
  let crc = 0xFFFF
  for (let i = 0; i < data.length; i++) {
    crc ^= data[i]
    for (let j = 0; j < 8; j++) {
      if ((crc & 1) !== 0) {
        crc = (crc >> 1) ^ 0xA001
      } else {
        crc = crc >> 1
      }
    }
  }
  return crc.toString(16).toUpperCase().padStart(4, '0')
}
</script>

<style scoped>
.calculator-container {
  font-family: Arial, sans-serif;
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.checksum-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

.checksum-table th,
.checksum-table td {
  border: 1px solid #ccc;
  padding: 10px;
  width: 150px;
  text-align: center;
}

textarea {
  width: 100%;
  margin-bottom: 10px;
  padding: 10px;
  font-family: monospace;
  resize: vertical;
}

.button-row {
  display: flex;
  justify-content: center;
  gap: 6px;
}

select, button {
  padding: 6px 12px;
  font-size: 14px;
}
</style>
