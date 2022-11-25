<template>
  <div>
    <div>
      <img src="@/assets/mvtisurvey/mvti7.jpg" alt="img">
    </div>
    <br>
    <div class="d-grid gap-2 col-6 mx-auto">
      <button class="btn btn-outline-primary" type="button" @click="toGroup5">50살에 의대가기</button>
      <button class="btn btn-outline-primary" type="button" @click="toGroup6">중학생으로 돌아가기 (2022년 그대로)</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup5() {
      this.$store.commit('TOGROUP3')
      this.$router.push({name: 'survey8'})
    }
    ,
    toGroup6() {
      this.$store.commit('TOGROUP4')
      this.$router.push({name: 'survey8'})
    }
  }
}
</script>

<style>

</style>