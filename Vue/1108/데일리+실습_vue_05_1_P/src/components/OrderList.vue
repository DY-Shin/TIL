<template>
  <div>
    <OrderListItem 
      v-for="(order, idx) in orderList" 
      :key="idx"
      :order="order"
    />
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'

export default {
  name: 'OrderList',
  components: {
    OrderListItem,
  },
  computed: {
    orderList: function () {
      return this.$store.state.orderList
    },
    totalOrderCount: function () {
      return this.$store.state.orderList[0].menu.price
    },
    totalOrderPrice: function () {
      return this.$store.state.orderList[0].menu.price
    },
  },
}
</script>

<style>
</style>