<template>
  <div class="base-converter " >
    <h1>进制转换（正整数）</h1>
    <p class="description">此转换支持的二进制数应满足1到32位，十进制数范围从0到4294967295。</p>
    
    <div class="input-group">
      <label for="binary">二进制 (base 2):</label>
      <input type="text" id="binary" v-model="binary" @input="convertFromBinary" 
             placeholder="例如: 1011111001110000001001011111100">
      <div v-if="binaryError" class="error-message">{{ binaryError }}</div>
    </div>
    
    <div class="input-group">
      <label for="octal">八进制 (base 8):</label>
      <input type="text" id="octal" v-model="octal" @input="convertFromOctal" 
             placeholder="例如: 13716011374">
      <div v-if="octalError" class="error-message">{{ octalError }}</div>
    </div>
    
    <div class="input-group">
      <label for="decimal">十进制 (base 10):</label>
      <input type="text" id="decimal" v-model="decimal" @input="convertFromDecimal" 
             placeholder="例如: 1597510396">
      <div v-if="decimalError" class="error-message">{{ decimalError }}</div>
    </div>
    
    <div class="input-group">
      <label for="hexadecimal">十六进制 (base 16):</label>
      <input type="text" id="hexadecimal" v-model="hexadecimal" @input="convertFromHexadecimal" 
             placeholder="例如: 5F3812FC">
      <div v-if="hexadecimalError" class="error-message">{{ hexadecimalError }}</div>
    </div>
    
    <el-button class="clear-button" @click="clearAll" type="danger" plain>清除</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      binary: '',
      octal: '',
      decimal: '',
      hexadecimal: '',
      binaryError: '',
      octalError: '',
      decimalError: '',
      hexadecimalError: ''
    };
  },
  methods: {
    convertFromBinary() {
      this.clearErrors();
      if (this.binary === '') {
        this.clearAll();
        return;
      }
      
      // 验证二进制输入
      if (!/^[01]+$/.test(this.binary)) {
        this.binaryError = '请输入有效的二进制数（只包含0和1）';
        return;
      }
      
      if (this.binary.length < 1 || this.binary.length > 99999999) {
        this.binaryError = '二进制数长度应为1-32位';
        return;
      }
      
      const num = parseInt(this.binary, 2);
      this.updateAllFields(num);
    },
    
    convertFromOctal() {
      this.clearErrors();
      if (this.octal === '') {
        this.clearAll();
        return;
      }
      
      if (!/^[0-7]+$/.test(this.octal)) {
        this.octalError = '请输入有效的八进制数（只包含0-7）';
        return;
      }
      
      const num = parseInt(this.octal, 8);
      if (num > 4294967295) {
        this.octalError = '数值超出32位无符号整数范围';
        return;
      }
      
      this.updateAllFields(num);
    },
    
    convertFromDecimal() {
      this.clearErrors();
      if (this.decimal === '') {
        this.clearAll();
        return;
      }
      
      if (!/^\d+$/.test(this.decimal)) {
        this.decimalError = '请输入有效的十进制数';
        return;
      }
      
      const num = parseInt(this.decimal, 10);
      if (num > 4294967295) {
        this.decimalError = '数值超出32位无符号整数范围（0-4294967295）';
        return;
      }
      
      this.updateAllFields(num);
    },
    
    convertFromHexadecimal() {
      this.clearErrors();
      if (this.hexadecimal === '') {
        this.clearAll();
        return;
      }
      
      if (!/^[0-9A-Fa-f]+$/.test(this.hexadecimal)) {
        this.hexadecimalError = '请输入有效的十六进制数（0-9, A-F）';
        return;
      }
      
      const num = parseInt(this.hexadecimal, 16);
      if (num > 4294967295) {
        this.hexadecimalError = '数值超出32位无符号整数范围';
        return;
      }
      
      this.updateAllFields(num);
    },
    
    updateAllFields(num) {
      if (isNaN(num)) return;
      
      this.binary = num.toString(2);
      this.octal = num.toString(8);
      this.decimal = num.toString(10);
      this.hexadecimal = num.toString(16).toUpperCase();
    },
    
    clearAll() {
      this.binary = '';
      this.octal = '';
      this.decimal = '';
      this.hexadecimal = '';
      this.clearErrors();
    },
    
    clearErrors() {
      this.binaryError = '';
      this.octalError = '';
      this.decimalError = '';
      this.hexadecimalError = '';
    }
  }
};
</script>

<style scoped>
.base-converter {
  font-family: Arial, sans-serif;
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.description {
  color: #666;
  font-size: 14px;
  margin-bottom: 20px;
}

.input-group {
  margin-bottom: 15px;
}

.input-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

.input-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.input-group input:focus {
  outline: none;
  border-color: #4a90e2;
  box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2);
}

.error-message {
  color: #e74c3c;
  font-size: 14px;
  margin-top: 5px;
}

</style>