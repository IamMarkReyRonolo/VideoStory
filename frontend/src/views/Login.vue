<template>
    <div>
        <h1>Todo App</h1>
        <div class="formWrapper">
            <v-text-field label="Todo" solo v-model="inputTodo"></v-text-field>
            <v-btn @click="addTodo()"> Add Todo </v-btn>
        </div>

		<h2>In Progress</h2>
		<div class="todoListWrapper">
			<div class="todo"  v-for="todo in todoList" :key="todo.id">
				<div class="todoDetails">{{todo.content}}</div>
				<div class="todoFunctions">
					<v-btn @click="doneTodo(todo)"> Done </v-btn>
					<v-btn> Update </v-btn>
					<v-btn @click="deleteTodo(todo)"> Delete </v-btn>
				</div>
			</div>
		</div>
		<hr>
		<br>
		<h2>Done List</h2>
		<div class="todoListDoneWrapper">
			<div class="todo"  v-for="todo in doneTodoList" :key="todo">
				<div class="todoDetails">{{ todo }}</div>
				<div class="todoFunctions">
					<v-btn @click="recoverTodo(todo)"> Recover </v-btn>
					<v-btn @click="deleteDoneTodo(todo)"> Delete </v-btn>
				</div>
			</div>
		</div>
    </div>
</template>

<script>
export default {
    name: "Login",
    data: () => ({
		todoList: [],
		inputTodo: "",
		inProgressTodo: [],
		doneTodoList: [],
		tempEditedTodo: ""
	}),
    created() {

	},

    methods: {
		addTodo() {
			let todo = {
				id: this.todoList.length,
				content: this.inputTodo,
				status: "in_progress"
			}

			this.todoList.push(todo)
			this.inputTodo = ""
			alert(`Todo ${this.inputTodo} is added to the list.`);
			
		},

		updateTodo(todo) {
			this.tempEditedTodo = todo
			this.inputTodo = todo
		},

		deleteTodo(id) {
			this.todoList.forEach((todo)=> {
				if (todo.id == id) {
					this.todoList.pop(todo)
				}
			})
			alert(`Todo ${todo} is deleted to the list.`);
			
		},

		doneTodo(todo) {
			this.inProgressTodo.pop(todo)
			this.doneTodoList.push(todo)
			alert(`Todo ${this.inputTodo} is moved to done list.`);
			
		},

		deleteDoneTodo(todo) {
			this.doneTodoList.pop(todo)
			alert(`Todo ${this.inputTodo} is deleted from done list.`);
		},

		recoverTodo(todo) {
			this.inProgressTodo.push(todo)
			this.doneTodoList.pop(todo)
			alert(`Todo ${this.inputTodo} is moved back to in progress.`);
			
		},
	},
    computed: {},
};
</script>

<style scoped>
.formWrapper {
    display: flex;
    justify-content: center;
    align-items: center;
	margin: 20px;
}

.v-btn {
	margin: 10px;
}

.todoListWrapper, .todoListDoneWrapper {
	margin: 20px
}

.todo {
	display: flex;
	align-items: center;
	/* width: 300px; */
	justify-content: space-between;
	border: 1px solid rgb(41, 41, 41);
	padding: 20px;
	border-radius: 10px;
	margin: 10px 0px;
}
</style>
