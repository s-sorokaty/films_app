const path = 'http://localhost:8000/'

export const apiPATH = {
    employee: path + 'employee/',
    client: path + 'client/',
    ageRaiting: path + 'age-raiting/',
    filmGenre: path + 'film-genre/',
    filmInfo: path + 'film-info/info/',
    genreOnFilm: path + 'film-info/genre/',
    place: path + 'place/',
    ticketInfo: path + 'ticket-info/',
    hall: path+ 'hall/',
    sessionInfo: path + 'session-info/session/',
    filmOnSession: path + 'session-info/session-film/'
}

export const apiSecondPATH = {
    coloums: 'coloums'
}

export const selectableColoums = {
    idClient: apiPATH.client,
    idEmployee: apiPATH.employee,
    idPlace: apiPATH.place,
    ageRaiting: apiPATH.ageRaiting,
    idGenre: apiPATH.filmGenre,
    idFilm: apiPATH.filmInfo,
    idHall: apiPATH.hall,
    idSession:apiPATH.sessionInfo,
    startTime:'DATE',
    endTime:'DATE'
}

export const apiSelector = [
    { value: 'employee', label: 'Управление Работниками', isSearching: false },
    { value: 'client', label: 'Управление Клиентами', isSearching: false },
    { value: 'ageRaiting', label: 'Возврастной рейтинг', isSearching: false },
    { value: 'filmGenre', label: 'Жанры', isSearching: false },
    { value: 'filmInfo', label: 'Информация о фильме', isSearching: false },
    { value: 'genreOnFilm', label: 'Жанры в фильме', isSearching: false },
    { value: 'place', label: 'Места', isSearching: false },
    { value: 'ticketInfo', label: 'Информация о билете', isSearching: false },
    { value: 'hall', label: 'Настройка залов', isSearching: false },
    { value: 'sessionInfo', label: 'Управление сессиями', isSearching: false },
    { value: 'filmOnSession', label: 'Настройка фильмов на сессии', isSearching: false },
    
]
export const API = {
    get: async (path, body = undefined) => {
        return fetch(path, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json;charset=utf-8',
            },
            body
        }, )

    },
    update: async (path, body) => {
        return fetch(path, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
            },
            body: JSON.stringify(body)
        })
    },
    delete: async (path, body) => {
        return fetch(path, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
            },
            body: JSON.stringify(body)
        })

    },
    post: async (path, body) => {
        return fetch(path, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
            },
            body: JSON.stringify(body)
        })

    }
}
