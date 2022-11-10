import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    list: [
			// 개별 todo Object
      {
        id: 1638771553377,                // nowDateObj.getTime()
        content: 'Vue',                   // Todo 내용
        dueDateTime: '2021-12-09T00:00',  // 마감일
        isCompleted: false,               // 완료된 할 일
        isImportant: true,				        // 중요 할 일
      },
      {
        id: 1638771553378,
        content: 'Vue Router',
        dueDateTime: '2021-12-10T00:00',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 16387715533779,
        content: 'Vuex',
        dueDateTime: '2021-12-11T00:00',
        isCompleted: true,
        isImportant: false,
      },
    ],
  },
  getters: {
  },
  mutations: {
    CREATE_TODO(state, Todo){
      state.list.push(Todo)
    },
    UPDATE_TODO_STATUS(state, todoItem){
      state.list.map(todo => {
        if(todo === todoItem){
          todoItem.isCompleted = !todoItem.isCompleted
        }
        return todo
      })
    },
    UPDATE_IMPORTANCE(state, todoItem){
      state.list.map(todo => {
        if(todo === todoItem){
          todoItem.isImportant = !todoItem.isImportant
        }
        return todo
      })
    },
  },
  actions: {
    createTodo(context, content) {
      const Todo = {
        id: new Date().getTime(),
        content: content,
        dueDateTime: new Date(context.id).toLocaleString,
        isCompleted: false,
        isImportant: false,
      }
      context.commit('CREATE_TODO', Todo)
    },
    updateTodoStatus(context, todoItem) {
      context.commit('UPDATE_TODO_STATUS', todoItem)
    },
    updateImportance(context, todoItem) {
      context.commit('UPDATE_IMPORTANCE', todoItem)
    },
  },
  modules: {
  }
})

