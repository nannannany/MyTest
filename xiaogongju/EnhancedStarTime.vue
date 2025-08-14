<template>
    <!-- 原始组件 -->
    <StarTime
      ref="originalConverter"
      :sourceCode="sourceCode"
      :baseTime="baseTime"
      :cumulativeSeconds="cumulativeSeconds"
      @convert="handleConvert"
    />
  <div class="wrapper-tip" v-if="showTip">
    提示：源码值需为十六进制字符串，基准时间格式为YYYY-MM-DDTHH:mm
  </div>

</template>

<script>
import StarTime from './StarTime.vue'; 

export default {
  name: 'StarTimeConverterWrapper',
  components: { StarTime },
  
  // 代理原始组件的响应式数据
  data() {
    return {
      sourceCode: '',
      baseTime: '',
      cumulativeSeconds: 0,
      showTip: true 
    };
  },

  // 代理原始组件的方法
  methods: {
    handleConvert() {
      // 可在此处添加前置校验或日志记录（非侵入式）
      console.log('开始转换，参数：', {
        sourceCode: this.sourceCode,
        baseTime: this.baseTime,
        cumulativeSeconds: this.cumulativeSeconds
      });
      
      this.$refs.originalConverter.convert();
    }
  }
};
</script>

<style scoped>
.wrapper-tip {
  margin-top: 15px;
  padding: 8px;
  background-color: #f8f9fa;
  border-radius: 4px;
  font-size: 0.9em;
  color: #6c757d;
}

</style>