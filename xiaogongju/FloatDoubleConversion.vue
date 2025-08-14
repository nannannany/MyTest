<template>
  <div class="ieee754-converter">
    <h1>浮点数转换</h1>
    <p>此转换支持32位单精度和64位双精度</p>
    <br>
    <div class="input-group">
      <label for="decimal-input">十进制</label>
      <input type="text" id="decimal-input" v-model="decimalInput" @input="convertFromDecimal">
    </div>

    <div class="converter-section">
      <h2>float 单精度 (32bit)</h2>
      <div class="input-group">
        <label for="float-decimal">十进制</label>
        <input type="text" id="float-decimal" v-model="floatDecimal" readonly>
      </div>
      <div class="input-group">
        <label for="float-binary">二进制</label>
        <input type="text" id="float-binary" v-model="floatBinary" readonly>
      </div>
      <div class="input-group">
        <label for="float-hex">十六进制</label>
        <input type="text" id="float-hex" v-model="floatHex" readonly>
      </div>
    </div>

    <div class="converter-section">
      <h2>doucle 双精度 (64bit)</h2>
      <div class="input-group">
        <label for="double-decimal">十进制</label>
        <input type="text" id="double-decimal" v-model="doubleDecimal" readonly>
      </div>
      <div class="input-group">
        <label for="double-binary">二进制</label>
        <input type="text" id="double-binary" v-model="doubleBinary" readonly>
      </div>
      <div class="input-group">
        <label for="double-hex">十六进制</label>
        <input type="text" id="double-hex" v-model="doubleHex" readonly>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      decimalInput: '',
      floatDecimal: '',
      floatBinary: '',
      floatHex: '',
      doubleDecimal: '',
      doubleBinary: '',
      doubleHex: ''
    };
  },
  methods: {
    convertFromDecimal() {
      if (!this.decimalInput) {
        this.resetFields();
        return;
      }

      try {
        const num = parseFloat(this.decimalInput);
        
        const floatBuffer = new ArrayBuffer(4);
        const floatView = new DataView(floatBuffer);
        floatView.setFloat32(0, num);
        this.floatDecimal = num.toFixed(8);
        this.floatBinary = this.bufferToBinary(floatBuffer, 32);
        this.floatHex = this.bufferToHex(floatBuffer, 4);

        const doubleBuffer = new ArrayBuffer(8);
        const doubleView = new DataView(doubleBuffer);
        doubleView.setFloat64(0, num);
        this.doubleDecimal = num.toFixed(16);
        this.doubleBinary = this.bufferToBinary(doubleBuffer, 64);
        this.doubleHex = this.bufferToHex(doubleBuffer, 8);
      } catch (e) {
        console.error('转换错误:', e);
        this.resetFields();
      }
    },
    bufferToBinary(buffer, bits) {
      let binary = '';
      const view = new DataView(buffer);
      for (let i = 0; i < buffer.byteLength; i++) {
        const byte = view.getUint8(i);
        binary += byte.toString(2).padStart(8, '0');
      }
      return binary.substring(0, bits);
    },
    bufferToHex(buffer, bytes) {
      let hex = '';
      const view = new DataView(buffer);
      for (let i = 0; i < bytes; i++) {
        const byte = view.getUint8(i);
        hex += byte.toString(16).padStart(2, '0');
      }
      return hex;
    },
    resetFields() {
      this.floatDecimal = '';
      this.floatBinary = '';
      this.floatHex = '';
      this.doubleDecimal = '';
      this.doubleBinary = '';
      this.doubleHex = '';
    }
  }
};
</script>

<style scoped>
.ieee754-converter {
  font-family: Arial, sans-serif;
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.converter-section {
  margin-bottom: 20px;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.input-group {
  margin-bottom: 10px;
}

.input-group label {
  display: inline-block;
  width: 120px;
  margin-right: 10px;
  vertical-align: top;
}

.input-group input {
  width: calc(100% - 130px);
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
