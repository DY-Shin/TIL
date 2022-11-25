<template>
  <div>
    <div>
      <img src="@/assets/mvtisurvey/mvti8.jpg" alt="img">
    </div>
    <br>
    <div class="d-grid gap-2 col-6 mx-auto">
      <button class="btn btn-outline-primary" type="button" @click="toGroup5">50% 확률로 5억 받기</button>
      <button class="btn btn-outline-primary" type="button" @click="toGroup6">그냥 5000만원 받기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup5() {
      this.$store.commit('TOGROUP3')
      this.$router.push({name: 'survey9'})
    }
    ,
    toGroup6() {
      this.$store.commit('TOGROUP4')
      this.$router.push({name: 'survey9'})
    }
  }
}
</script>

<style>

</style>