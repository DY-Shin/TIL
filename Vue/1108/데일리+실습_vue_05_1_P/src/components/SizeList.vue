<template>
  <div class="size-list">
    <h1>2. 사이즈를 고르세요.</h1>
    <SizeListItem
      v-for="(size, idx) in sizeList"
      :key="idx"
      :size="size"
    />
  </div>
</template>

<script>
import SizeListItem from '@/components/SizeListItem'

export default {
  name: 'SizeList',
  components: {
    SizeListItem,
  },
  computed: {
    sizeList: function () {
      return this.$store.state.sizeList
    },
  },
}
</script>

<style>
  .size-list{
    background-color: white;
    margin: 0 auto;
    border-radius: 25px;
  }
</style>