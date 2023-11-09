import plotly.graph_objects as go

# Sample data
categories = ['Category A', 'Category B', 'Category C']
values1 = [10, 15, 5]
values2 = [5, 10, 15]
values3 = [8, 12, 4]

fig = go.Figure()

# Create the stacked bar chart
fig.add_trace(go.Bar(x=categories, y=values1, name='Value 1'))
fig.add_trace(go.Bar(x=categories, y=values2, name='Value 2'))
fig.add_trace(go.Bar(x=categories, y=values3, name='Value 3'))

# Customize hover labels
hover_text = []
for cat, val1, val2, val3 in zip(categories, values1, values2, values3):
    hover_text.append(f'{cat}<br>Value 1: {val1}<br>Value 2: {val2}<br>Value 3: {val3}')

fig.update_traces(text=hover_text, hoverinfo='text+name')

# Customize the layout
fig.update_layout(
    barmode='stack',
    xaxis_title='Categories',
    yaxis_title='Values',
    title='Stacked Bar Graph with Hover Labels'
)

# Show the interactive graph
fig.show()
