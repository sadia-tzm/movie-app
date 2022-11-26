<template>
    <div class="border rounded bg-success shadow p-4 mt-5 text-white">
        <h3 class="text-white">Update a movie!</h3>
        <div>
            <label class="m-2">Movie Title</label>
            <input class="form-control" v-model="title" placeholder="Movie Title" type="text" />
            <label class="m-2">Date Released</label>
            <input class="form-control" v-model="date_released" placeholder="Date Released" type="date" />
            <label class="m-2">Rating</label>
            <input class="form-control" v-model="rating" placeholder="Rating" type="number" />
            <label class="m-2">Award Winning</label>
            <input class="form-control" v-model="award_winning" placeholder="Award Winning" type="text" />
            <div class="dropdown">
                <button @click="get_movie_ids" class="btn btn-dark dropdown-toggle mt-2" type="button" data-bs-toggle="dropdown">Movie IDs
                    <span class="caret"></span></button>
                <ul class="dropdown-menu">
                        <li v-for="movie in movies"><a href="#">{{ movie.id }}</a></li>
                </ul>
            </div>
            <label class="m-2">Input Movie ID</label>
            <input class="form-control" v-model="movie_id" placeholder="Movie ID" type="number" />
            <button @click="update_movie(parseInt(movie_id), title.toString(), parseInt(rating), award_winning.toString())" type="submit" class="btn btn-dark m-2">Update</button>
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
        async update_movie(movie_id, title, rating, award_winning) {
            console.log(movie_id)
            let response = await fetch("http://127.0.0.1:8000/api/movies/" + movie_id + "/", {
                method: 'PUT',
                body: JSON.stringify({
                    'id': movie_id,
                    'title': title,
                    'date_released': this.date_released,
                    'rating': rating,
                    'award_winning': award_winning,
                }),
                headers: {
                    'Content-Type': 'application/json',
                }

            })
            .then(response => response.json())
            .then(json => console.log(json))
        }
    }
}


</script>