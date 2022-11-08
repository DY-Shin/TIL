<template>
  <ul>
    <li 
      :class="{ 'selected': size.selected }" 
      @click="onSelectMenu"
    >
      <span>
        {{ size.name }}
        {{ size.price }}원
      </span>
    </li>
  </ul>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods: {
    onSelectMenu: function () {
      this.$store.dispatch('updateSizeList', this.size)
    },
  },
}
</script>

<style>
  .selected{
    background-color: green;
    color: white;
  }
</style>