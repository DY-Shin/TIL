<template>
  <ul>
    <li 
      :class="{ 'selected': menu.selected }" 
      @click="selectMenu"
    >
      <span>
        <img :src="menu.image" alt="" width="50px" height="50px">
        {{ menu.title }}
        {{ menu.price }}원
      </span>
    </li>
  </ul>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    selectMenu: function () {
      this.$store.dispatch('updateMenuList', this.menu)
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