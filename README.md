# tmple
General files or content generator, using **template** and **data/variables**.

> Content of the file will be controlled by the **template** (in [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)), 
and you can control the **template** using **data/variables** (in [Yaml](https://yaml.org/)).
## Use cases
#### 👨‍👩‍👦 Generate simple file, based on a template
Let say you want to generate a repeated SQL file like this:
```sql

WITH 
top_user (SELECT name, phone, address, gender, birth_date FROM top_user LIMIT 10),
mid_user (SELECT name, phone, address, gender, birth_date FROM mid_user LIMIT 10),
low_user (SELECT name, phone, address, gender, birth_date FROM low_user LIMIT 10),
base_user (SELECT name, phone, address, gender, birth_date FROM base_user LIMIT 10)

SELECT * top_user UNION ALL
SELECT * mid_user UNION ALL
SELECT * low_user UNION ALL
SELECT * base_user
```
<sub><sup>**just imagine it has 1000 lines with another repetitive complex query* </sup></sub>😂

Now, what you need to do, is having a template! a Jinja template!
```django
WITH 
{%- for tb in tables %}
{{ tb.name }} AS (SELECT {% for c in columns %}{{ c }}{{ ',' if not loop.last }} {% endfor %}FROM {{ tb.name }} LIMIT {{ tb.limit }}){{ ',' if not loop.last }}
{%- endfor %}
{% for tb in tables %}
SELECT * FROM {{ tb.name }} {{ 'UNION ALL' if not loop.last }}
{%- endfor %}
```
<sub><sup>*Save it to `.jinja2` file to your folder `working_dir/sample.jinja2`*</sup></sub>

But for sure that 👆 template can't generate by it self, it needs a data or variables to work on, right?
Let's just create a yaml file with this format:

```yaml
var: #hold all variables/dictionary that needed in your jinja files
    tables:
        - name: top_user
        limit: 10
        - name: mid_user
        limit: 20
        - name: low_user
        limit: 10
        - name: base_user
        limit: 30

    columns:
        - name
        - phone
        - address
        - gender
        - birth_date

generator:
    - template: sample.jinja2 #where you save your jinja file
      destination:
        - output.sql
        - log # to also print the result on your terminal
```
<sub><sup>*Save it to `.yaml` file to your folder as `working_dir/recipe.yaml`*</sup></sub>
Done! above yaml is what we call `recipe`, for more detail, please take a look here.
Now, lets run your recipe!
```bash
cd working_dir

tmple --recipe recipe.yaml
```

Uh oh, you can't run tmple yet? install first man! 😂😂

#### Generate list of files based on multiple templates

#### Nested variables

#### Just print, not generate files

#### Recipe concept
Recipe is a config file to tell the `tmple` about:
- all the variables that needed in your **templates** (`var:`)
- which template that you gonna use to generate file (`generator:template:`)
- where to save the generated content from your template (`generator:destination:`)


```yaml
var: # mandatory
    any_variable: you need
    you_can:
        - write
        - down
        - here
    and_also:
        it_support: 
            nested: variables!
# above variables it just mentionable in the Jinja files
# like {{ it_also.support.nested }}

extend: # optional
    - samples/recipes/parent_recipe.yaml
    # do inherit
    # all variables or generator written from this parent_recipe.yaml 
    # will be also extended into current recipe
    

generator: # mandatory
    - template: samples/templates/sample.jinja2
      destination:
        - samples/results/sample.sql # directly create a file in this relateve path
        - /Users/personname/folder/tmple/src/results/simple.sql #absolute path to place to some folder
        - log # just print in the log of your terminal

    # you could also generate multiple files in different template using the same variables
    - template: samples/templates/sample2.jinja2
    # if there is no destination key here, then it will only print the generated content
```

## Usage

### Install via pip

### run
