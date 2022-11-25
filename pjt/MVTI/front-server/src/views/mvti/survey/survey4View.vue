<template>
  <div>
    <div>
      <img src="@/assets/mvtisurvey/mvti4.jpg" alt="img">
    </div>
    <br>
    <div class="d-grid gap-2 col-6 mx-auto">
      <button class="btn btn-outline-primary" type="button" @click="toGroup3">부모님에게 내 수명 5년 주기</button>
      <button class="btn btn-outline-primary" type="button" @click="toGroup4">그냥 내 수명대로 살기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup3() {
      this.$store.commit('TOGROUP2')
      this.$router.push({name: 'survey5'})
    }
    ,
    toGroup4() {
      this.$store.commit('TOGROUP6')
      this.$router.push({name: 'survey5'})
    }
  }
}
</script>

<style>

</style>