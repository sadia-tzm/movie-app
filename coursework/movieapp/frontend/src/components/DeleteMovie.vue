<template>
    <div class="border rounded bg-primary shadow p-4 mt-5 text-white">
        <h3>Delete a movie!</h3>
        <div>
            <div class="dropdown">
                <button @click="get_movie_ids" class="btn btn-dark dropdown-toggle" type="button" data-bs-toggle="dropdown">Movie IDs
                    <span class="caret"></span></button>
                <ul class="dropdown-menu">
                        <li v-for="movie in movies"><a href="#">{{ movie.id }}</a></li>
                </ul>
            </div>
            <label class="m-2">Input Movie ID</label>
            <input class="form-control" v-model="movie_id" placeholder="Movie ID" type="number" />
            <button @click="delete_movie(parseInt(movie_id))" type="submit" class="btn btn-dark m-2">Delete</button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            movies: [],
            title: [],
            date_released: [],
            rating: [],
            award_winning: [],
            movie_id: [],
        }
    },
    methods: {
        async get_movie_ids() {
            let response = await fetch("http://127.0.0.1:8000/api/movies/");
            let data = await response.json();
            this.movies = data.movies;
        },
        async delete_movie(movie_id) {
            console.log(movie_id)
            // DELETE movie using fetch API
            let response = await fetch("http://127.0.0.1:8000/api/movies/" + movie_id, {
                method: "DELETE",
            })
            if (response.ok) {
                this.movies = this.movies.filter(m => m.id != movie.id)
            }
            else
                alert("Deleting movie failed")
        },
    },
    headers: {
                    'Content-Type': 'application/json',
                }
}
</script>