const path = 'http://localhost:8000/'
const apiPATH = {
    employee: path + 'employee/',
    client: path + 'client',
    ageRaiting: path + 'age-raiting',
    filmGenre: path + 'film-genre',
    filmInfo: path + 'film-info/info',
    genreOnFilm: path + 'film-info/genre',
    place: path + 'place',
    ticketInfo: path + 'ticket-info'
}

const API = {
    get: async (path, body = undefined) => {
        return fetch(path, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json;charset=utf-8',
            },
        })

    }
}

