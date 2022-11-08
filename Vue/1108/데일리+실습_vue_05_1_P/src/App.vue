<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <div class="container">
      <MenuList/>
      <SizeList/>
    </div>
    <button @click="order">장바구니 담기</button>
    <OrderList/>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OrderList
  },
  methods: {
    order() {
      this.$store.commit('addOrder')
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0 auto;
  text-align: center;
  justify-content: space-between;
}

.container {
  width: 800px;
  border: solid 10px rgb(202, 202, 202);
  background-color: rgb(202, 202, 202);
  border-radius: 25px;
  display: flex;
  justify-content: center;
}

ul {
  list-style: none;
}
</style>
