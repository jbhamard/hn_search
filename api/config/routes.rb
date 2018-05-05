Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  date_regexp = /\d\d\d\d(?:(?:(-(0[1-9]|1[0-2]))?)(?:-(0[1-9]|[12][0-9]|3[01])?)?)(?:(?:(?:\%20([0-1]\d|[2][0-3])?)(?:\:?)(?:([0-5]\d)?)(?:\:([0-5]\d)?)?)?)/

  get '/1/queries/count/:date', to: 'queries#count', constraints: {date: date_regexp}
  get '/1/queries/popular/:date', to:'queries#popular', constraints: {date: date_regexp}
end