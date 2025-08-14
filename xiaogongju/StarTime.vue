<template>
  <div class="star-time-converter">
    <h1>星时转换器</h1>
    <br>
    <table>
      <thead>
        <tr>
          <th>源码值</th>
          <th>星时基准</th>
          <th>累计秒</th>
          <th>工程值</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><input type="text" v-model="sourceCode" placeholder="输入源码值" /></td>
          <td>
            <input type="datetime-local" v-model="baseTime" />
          </td>
          <td><input type="number" v-model.number="cumulativeSeconds" placeholder="输入累计秒" /></td>
          <td>{{ engineeringValue }}</td>
        </tr>
      </tbody>
    </table>
    <el-button @click="convert" type="primary" plain>转换</el-button>
  </div>


</template>

<script>
import dayjs from 'dayjs';

export default {
  name: 'StarTimeConverter',
  data() {
    return {
      sourceCode: '', // 源码值
      baseTime: '', // 星时基准
      cumulativeSeconds: 0, // 累计秒
      engineeringValue: '', // 工程值
    };
  },
  methods: {
    convert() {
      if (!this.sourceCode || !this.baseTime || this.cumulativeSeconds === 0) {
        alert('请填写所有输入字段');
        return;
      }
      const sourceNum = parseInt(this.sourceCode, 16);
      if (isNaN(sourceNum)) {
        alert('无效的源码值');
        return;
      }
      // 解析基准时间
      const baseDate = dayjs(this.baseTime);
      if (!baseDate.isValid()) {
        alert('无效的基准时间');
        return;
      }
      // 计算工程值
      const targetDate = baseDate.add(this.cumulativeSeconds, 'second');
      this.engineeringValue = targetDate.format('YYYY-MM-DD HH:mm:ss');
    },
  },
};
</script>

<style scoped>
.star-time-converter {
  font-family: Arial, sans-serif;
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
table {
  width: 100%;
  border-collapse: collapse;
  table-layout: auto;
}
th, td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: center;
  white-space: nowrap;
}
input {
  width: 90%;
  padding: 4px;
}
button {
  display: block;
  margin: 20px auto;
  padding: 10px 20px;
}

</style>
