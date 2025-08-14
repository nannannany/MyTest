<template>
  <div class="checksum-wrapper">
    <HexadecimalCheck
      v-bind="$props"
    />
  </div>
</template>

<script>
import HexadecimalCheck from './HexadecimalCheck.vue'; 

export default {
  name: 'EnhancedHexadecimalCheck',
  components: { HexadecimalCheck },
  
  props: {
  },
  
  // 代理所有事件
  emits: ['any-event-you-want-to-capture'],
  
 
  setup(props, { emit }) {
    // 可以在这里添加非侵入式的逻辑：
    return {};
  }
};
</script>

<style scoped>
</style>