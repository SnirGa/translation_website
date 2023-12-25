<template>
  <div class="main">
    <img src="../assets/cover_image.jpg" width="400px" id="coverImage">
    <div id="searchInputWrapper">
      <b-form-input id="searchInput" v-model="userInput" placeholder="Enter word"></b-form-input>
      <b-button @click="SearchWord">Search</b-button>
      
    </div>
    <div id="responseWrapper">
      <b-container id="container">
        <b-row>
          <b-col>
            <b-list-group v-if='this.translation!=""'>
              <b-list-group-item class="headers">Translation</b-list-group-item>
              <b-list-group-item class="dataItems">{{this.translation[0]}}</b-list-group-item>
            </b-list-group>         
          </b-col>
          <b-col>         
            <b-list-group v-if='this.examples!=""'>
              <b-list-group-item class="headers">Examples</b-list-group-item>
              <b-list-group-item v-for="(item, index) in examples" :key="index" v-html="item[0]" class="dataItems"></b-list-group-item>
            </b-list-group>
            
          </b-col>
        </b-row>
      </b-container >
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchComp',
  props: {
    msg: String
  },
  data() {
    return {
      userInput: '',
      showSpinner: false,
      translation:"",
      examples:""
    };
  },
  methods: {
    async SearchWord() {
      this.translation="";
      this.examples="";
      let url="http://127.0.0.1:5000/search?word="+this.userInput
      const response = await fetch(url);
      const data = await response.json();
      this.translation=JSON.parse(JSON.stringify(data)).translation
      this.examples=JSON.parse(JSON.stringify(data)).examples
    }
  }
}
</script>

<style scoped>
#searchInput{
  background-color: aliceblue;
  width: 20%;
  height: 30px; 
  margin:20px;
}
#searchInputWrapper{
  display: flex;
  justify-content: center;
  align-items: center;
}
.flags{
  height: 100px;
}
#container{
  width: 40%;
}
.headers{
  background-color: bisque;
}
.dataItems{
  background-color:beige

}
#coverImage{
  border-radius: 40px;
}

</style>
