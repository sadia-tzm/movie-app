<template>
    <div class="border rounded bg-info shadow p-4 text-white">
        <h3>Add a new movie!</h3>
        <div>
            <label class="m-2">Movie Title</label>
            <input class="form-control" v-model="title" placeholder="Movie Title" type="text" />
            <label class="m-2">Date Released</label>
            <input class="form-control" v-model="date_released" placeholder="Date Released" type="date" />
            <label class="m-2">Rating</label>
            <input class="form-control" v-model="rating" placeholder="Rating" type="number" />
            <label class="m-2">Award Winning</label>
            <input class="form-control" v-model="award_winning" placeholder="Award Winning" type="text" />
            <button @click="add_movie" type="submit" class="btn btn-dark m-2">Add</button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            title: [],
            date_released: [],
            rating: [],
            award_winning: [],
        }
    },
    methods: {
        async add_movie() {
            let response = await fetch("http://127.0.0.1:8000/api/movies/", {
                method: 'POST',
                body: JSON.stringify({
                    'title': this.title,
                    'date_released': this.date_released,
                    'rating': this.rating,
                    'award_winning': this.award_winning,
                }),
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(json => console.log(json));
        }
    }
}
</script>