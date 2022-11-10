<template>
  <div id="nav">
    <router-link :to="{ name: 'all' }">모든</router-link>
    <router-link :to="{ name: 'today' }">오늘</router-link>
    <router-link :to="{ name: 'important' }">중요</router-link>
  </div>
</template>

<script>
export default {
  name: 'SideBar',
}
</script>

<style>
#nav {
  border-radius: .5rem;
  border: 2px solid #2c3e50;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
}

#nav a {
  text-decoration: none;
  color: #2c3e50;
  font-size: 2rem;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>