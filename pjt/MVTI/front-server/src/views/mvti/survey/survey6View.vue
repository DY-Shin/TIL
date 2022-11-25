<template>
  <div>
    <div>
      <img src="@/assets/mvtisurvey/mvti6.jpg" alt="img">
    </div>
    <br>
    <div class="d-grid gap-2 col-6 mx-auto">
      <button class="btn btn-outline-primary" type="button" @click="toGroup3">무매력 히어로 되기</button>
      <button class="btn btn-outline-primary" type="button" @click="toGroup4">능력 쎈 악역 되기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'survey1View',
  methods: {
    toGroup3() {
      this.$store.commit('TOGROUP2')
      this.$router.push({name: 'survey7'})
    }
    ,
    toGroup4() {
      this.$store.commit('TOGROUP6')
      this.$router.push({name: 'survey7'})
    }
  }
}
</script>

<style>

</style>