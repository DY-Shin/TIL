<template>
  <li>
    <img :src="order.menu.image" alt="" width="50px" height="50px">
    {{ order.menu.title }}
    <br>
    사이즈: {{ order.size.name }}
  </li>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    totalPrice: function () {
      return this.$store.state.orderList[0].price
    },
  },
}
</script>

<style>
</style>