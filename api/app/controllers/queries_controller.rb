class QueriesController < ApplicationController
  before_action :set_date_path

  def count
    if @date
      render json: {count: matched_queries.length}, status: :ok
    else
      head :not_found
    end
  end

  def popular
    @size = (params[:size] || 3).to_i
    if @date
      queries = matched_queries.sort_by {|k,v| v}.reverse[0,@size].map do |item|
        {
          query: $queries_index[item[0]],
          count: item[1]
        }
      end
      render json: {queries: queries}, status: :ok
    else
      head :not_found
    end
  end

  private

  def matched_queries
    @date.reduce($date_index) {|q, key| q[key] || {'queries' => {}} }['queries']
  end

  def set_date_path
    date_string = params[:date]

    if !date_string
      @date = nil
    else
      time_path = []
      space_split = date_string.split(' ')
      if space_split.size == 2
       time_path = parse_time(space_split[1])
      end

      date_path = parse_date(space_split[0])

      @date = (date_path + time_path).compact
    end
  end

  def parse_time(time_string)
    time_string.split(':').map do |step|
      step.slice(0) == '0' ? step.slice(1) : step
    end
  end

  def parse_date(date_string)
    date_string.split('-').map.with_index do |step, i|
      if i > 0
        step.slice(0) == '0' ? step.slice(1) : step
      else
        step
      end
    end
  end
end