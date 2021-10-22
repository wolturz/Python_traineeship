from behave import *

def add_line_to_file(context, this_line):
  context.f.write(this_line + "\n")

def line_length(context):
    context.f.close()
    context.r = open(context.filename,'r')
    line_count = 0
    for line in context.r:
        if line != '\n':
            line_count += 1
    context.r.close()
    
    return line_count

@given('There is an empty text file available to us')
def step_impl(context):
    context.filename = 'data_tables.txt'
    context.f = open(context.filename,"wt")
    context.f.close()

@when('I open this file')
def step_impl(context):
    context.f = open(context.filename,"at")


@when('I write the following table in it')
def step_impl(context):
    for row in context.table:
        course = row["course"]
        participant = row["participants"]
        line = course + "\t" + participant
        add_line_to_file(context, line)


@then(u'This file has {number} lines in it')
def step_impl(context,number):
    assert line_length(context) == int(number)

    

@given('The text file has been opened')
def step_impl(context):
    context.filename = 'data_tables.txt'
    context.f = open(context.filename,'at')

@then(u'I write the values {one}, {two} and {three}')
def step_impl(context, one, two, three):
    line = one + '\t' + two + '\t' + three
    add_line_to_file(context,line)

@then('I close the file')
def step_impl(context):
    context.f.close()