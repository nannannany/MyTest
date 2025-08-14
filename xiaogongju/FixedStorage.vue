<template>
  <div class="container">
    <h1>单位转换器</h1>
    <br>
    <div class="input-group">
      <label for="bit">位 (bit):</label>
      <input type="number" id="bit" v-model.number="bit" @input="convertFromBit">
    </div>
    <div class="input-group">
      <label for="bytes">字节 (bytes):</label>
      <input type="number" id="bytes" v-model.number="bytes" @input="convertFromBytes">
    </div>
    <div class="input-group">
      <label for="kb">千字节 (KB):</label>
      <input type="number" id="kb" v-model.number="kb" @input="convertFromKB">
    </div>
    <div class="input-group">
      <label for="mb">兆字节 (MB):</label>
      <input type="number" id="mb" v-model.number="mb" @input="convertFromMB">
    </div>
    <div class="input-group">
      <label for="gb">吉字节 (GB):</label>
      <input type="number" id="gb" v-model.number="gb" @input="convertFromGB">
    </div>
    <div class="button-container">
      <el-button @click="resetAll" type="danger" plain>全部重置</el-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      bit: null,
      bytes: null,
      kb: null,
      mb: null,
      gb: null
    };
  },
  methods: {
    convertFromBit() {
      if (this.bit !== null && this.bit !== undefined) {
        this.bytes = this.bit / 8;
        this.kb = this.bytes / 1024;
        this.mb = this.kb / 1024;
        this.gb = this.mb / 1024;
      }
    },
    convertFromBytes() {
      if (this.bytes !== null && this.bytes !== undefined) {
        this.bit = this.bytes * 8;
        this.kb = this.bytes / 1024;
        this.mb = this.kb / 1024;
        this.gb = this.mb / 1024;
      }
    },
    convertFromKB() {
      if (this.kb !== null && this.kb !== undefined) {
        this.bytes = this.kb * 1024;
        this.bit = this.bytes * 8;
        this.mb = this.kb / 1024;
        this.gb = this.mb / 1024;
      }
    },
    convertFromMB() {
      if (this.mb !== null && this.mb !== undefined) {
        this.kb = this.mb * 1024;
        this.bytes = this.kb * 1024;
        this.bit = this.bytes * 8;
        this.gb = this.mb / 1024;
      }
    },
    convertFromGB() {
      if (this.gb !== null && this.gb !== undefined) {
        this.mb = this.gb * 1024;
        this.kb = this.mb * 1024;
        this.bytes = this.kb * 1024;
        this.bit = this.bytes * 8;
      }
    },
    resetAll() {
      this.bit = null;
      this.bytes = null;
      this.kb = null;
      this.mb = null;
      this.gb = null;
    }
  }
};
</script>

<style scoped>
.container {
  font-family: Arial, sans-serif;
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.input-group {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.input-group label {
  white-space: nowrap;
  display: inline-block;
  width: 120px;
  margin-right: 8px;
}

.input-group input {
  width: 100%;
  padding: 10px;

  border: 1px solid #ddd;
  border-radius: 4px;
}

.button-container {
  text-align: right;
}
</style>
