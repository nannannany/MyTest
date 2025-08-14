<template>
  <div class="ieee754-wrapper">
    <FloatDoubleConversion
      :decimalInput="decimalInput"
      :floatDecimal="floatDecimal"
      :floatBinary="floatBinary"
      :floatHex="floatHex"
      :doubleDecimal="doubleDecimal"
      :doubleBinary="doubleBinary"
      :doubleHex="doubleHex"
      @input="handleInput"
    />
  </div>
</template>

<script setup>
import FloatDoubleConversion from './FloatDoubleConversion.vue'; // 原始组件
import { ref } from 'vue';

// 代理原始组件的数据
const decimalInput = ref('');
const floatDecimal = ref('');
const floatBinary = ref('');
const floatHex = ref('');
const doubleDecimal = ref('');
const doubleBinary = ref('');
const doubleHex = ref('');

function handleInput(event) {
  decimalInput.value = event.target.value;
}
</script>

<style scoped>
.ieee754-wrapper {

}
</style>