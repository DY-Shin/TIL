<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" v-model="parentData" @keyup.enter="parentDataInput">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <AppChild 
      @child-input="childDataInput"
      :appData="appData"
      :parentData="parentData"
      :childData="childData"
    />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  props: {
    appData: String,
    childData: String,
  },
  components: {
    AppChild,
  },
  data() {
    return{
      parentData: null,
    }
  },
  methods:{
    childDataInput(childData){
      this.$emit('child-input', childData)
    },
    parentDataInput(){
      this.$emit('parent-input', this.parentData)
    }
  }
}
</script>

<style>

</style>