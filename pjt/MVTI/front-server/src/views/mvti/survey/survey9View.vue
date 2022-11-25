<template>
  <div>
    <div>
      <img src="@/assets/mvtisurvey/mvti9.jpg" alt="img">
    </div>
    <br>
    <div class="d-grid gap-2 col-6 mx-auto">
      <button class="btn btn-outline-primary" type="button" @click="toGroup5">과제 대신해주는 토니 스타크</button>
      <button class="btn btn-outline-primary" type="button" @click="toGroup6">밥 잘 사주는 이상형</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup5() {
      this.$store.commit('TOGROUP3')
      this.$store.dispatch('get_result')
      this.$router.push({name: 'MvtiResult'})
    },
    toGroup6() {
      this.$store.commit('TOGROUP4')
      this.$store.dispatch('get_result')
      this.$router.push({name: 'MvtiResult'})
    }
  }
}
</script>

<style>

</style>