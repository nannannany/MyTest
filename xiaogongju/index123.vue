<template>
  <div class="min-h-screen bg-gray-50 flex flex-col">
    <header class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-6 shadow-lg">
      <div class="container mx-auto">
        <h1 class="text-[clamp(1.8rem,3vw,2.5rem)] font-bold tracking-tight">工具导航</h1>
        <p class="text-blue-100 mt-2 text-lg">选择你需要的工具</p>
      </div>
    </header>
    <main class="flex-grow container mx-auto px-4 py-8">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        <router-link to="/AlarmClock" class="tool-card">
          <div class="bg-white rounded-xl shadow-md overflow-hidden transform transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
            <div class="bg-blue-500 p-4 text-white">
              <i class="fa fa-clock-o text-2xl"></i>
            </div>
            <div class="p-5">
              <h3 class="font-semibold text-lg mb-2">闹钟</h3>
              <p class="text-gray-600 text-sm">设置提醒时间，准时提醒</p>
            </div>
          </div>
        </router-link>

        <router-link to="/EnhancedBaseConversion" class="tool-card">
          <div class="bg-white rounded-xl shadow-md overflow-hidden transform transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
            <div class="bg-green-500 p-4 text-white">
              <i class="fa fa-exchange text-2xl"></i>
            </div>
            <div class="p-5">
              <h3 class="font-semibold text-lg mb-2">进制转换</h3>
              <p class="text-gray-600 text-sm">在不同进制间进行转换</p>
            </div>
          </div>
        </router-link>

        <router-link to="/EnhancedFloatDoubleConversion" class="tool-card">
          <div class="bg-white rounded-xl shadow-md overflow-hidden transform transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
            <div class="bg-yellow-500 p-4 text-white">
              <i class="fa fa-calculator text-2xl"></i>
            </div>
            <div class="p-5">
              <h3 class="font-semibold text-lg mb-2">浮点数计算</h3>
              <p class="text-gray-600 text-sm">精确计算浮点数</p>
            </div>
          </div>
        </router-link>

        <router-link to="/EnhancedHexadecimalCheck" class="tool-card">
          <div class="bg-white rounded-xl shadow-md overflow-hidden transform transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
            <div class="bg-red-500 p-4 text-white">
              <i class="fa fa-check-square-o text-2xl"></i>
            </div>
            <div class="p-5">
              <h3 class="font-semibold text-lg mb-2">校验和计算</h3>
              <p class="text-gray-600 text-sm">计算并验证数据的校验和</p>
            </div>
          </div>
        </router-link>

        <router-link to="/EnhancedStarTime" class="tool-card">
          <div class="bg-white rounded-xl shadow-md overflow-hidden transform transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
            <div class="bg-purple-500 p-4 text-white">
              <i class="fa fa-star-o text-2xl"></i>
            </div>
            <div class="p-5">
              <h3 class="font-semibold text-lg mb-2">星时计算</h3>
              <p class="text-gray-600 text-sm">计算天文相关的星时</p>
            </div>
          </div>
        </router-link>

        <router-link to="/EnhancedFixedStorage" class="tool-card">
          <div class="bg-white rounded-xl shadow-md overflow-hidden transform transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
            <div class="bg-pink-500 p-4 text-white">
              <i class="fa fa-database text-2xl"></i>
            </div>
            <div class="p-5">
              <h3 class="font-semibold text-lg mb-2">固存大小转换</h3>
              <p class="text-gray-600 text-sm">在不同存储单位间进行转换</p>
            </div>
          </div>
        </router-link>

        <router-link to="/EnhancedFrameScrambler" class="tool-card">
          <div class="bg-white rounded-xl shadow-md overflow-hidden transform transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
            <div class="bg-teal-500 p-4 text-white">
              <i class="fa fa-random text-2xl"></i>
            </div>
            <div class="p-5">
              <h3 class="font-semibold text-lg mb-2">数据加解扰</h3>
              <p class="text-gray-600 text-sm">对数据进行加扰和解扰操作</p>
            </div>
          </div>
        </router-link>

        <router-link to="/EnhancedCrcCalculator" class="tool-card">
          <div class="bg-white rounded-xl shadow-md overflow-hidden transform transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
            <div class="bg-orange-500 p-4 text-white">
              <i class="fa fa-shield text-2xl"></i>
            </div>
            <div class="p-5">
              <h3 class="font-semibold text-lg mb-2">CRC计算器</h3>
              <p class="text-gray-600 text-sm">计算循环冗余校验值</p>
            </div>
          </div>
        </router-link>
      </div>
    </main>
    <footer class="bg-gray-800 text-white py-6">
      <div class="container mx-auto px-4 text-center">
        <p>&copy; 2025 工具导航页 | 设计与开发</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>

</style>
