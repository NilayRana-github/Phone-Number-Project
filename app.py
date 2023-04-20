# importing lib
from flask import Flask, render_template, request, redirect, url_for
import phonenumbers
from phonenumbers import geocoder
from geopy.geocoders import Nominatim
import folium
from phonenumbers import carrier
# import pycountry

# app name
app = Flask(__name__)


def get_location_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, "CH")
        country_name = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")
        geolocator = Nominatim(user_agent="myapp")
        location = geolocator.geocode(
            country_name + phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164))
        return {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "country_name": country_name,
            "service_provider": service_provider
        }
    except:
        return None


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        phone_number = request.form["phone_number"]
        location_info = get_location_info(phone_number)
        if location_info:
            return render_template("info.html", phone_number=phone_number, location_info=location_info)
        else:
            return render_template("error.html", message="Invalid phone number")
    else:
        return render_template("index.html")


@app.route("/map")
def show_map():
    phone_number = request.args.get("phone_number")
    location_info = get_location_info(phone_number)
    if location_info:
        map = folium.Map(location=[location_info["latitude"], location_info["longitude"]], zoom_start=10)
        folium.Marker(location=[location_info["latitude"], location_info["longitude"]], popup=phone_number).add_to(map)
        return map._repr_html_()
    else:
        return "Invalid phone number"


if __name__ == '__main__':
    app.run(debug=True)

# 2nd code

#
# import pycountry
# # importing lib
# from flask import Flask, render_template, request, redirect, url_for
# import phonenumbers
# from geopy.geocoders import Nominatim
# import folium
# from phonenumbers import carrier
#
# # app name
# app = Flask(__name__)
#
# # list of countries
# from pycountry import countries
# # countries = sorted(countries, key=lambda x: x['name'])
#
# def get_location_info(phone_number, country_code):
#     try:
#         parsed_number = phonenumbers.parse(phone_number,  pycountry.countries.get(alpha_2=country_code).alpha_2)
#         service_provider = carrier.name_for_number(parsed_number, "en")
#         geolocator = Nominatim(user_agent="myapp")
#         location = geolocator.geocode(
#             f"{countries.get(alpha_2=country_code).name} " + phonenumbers.format_number(parsed_number,
#                                                                                         phonenumbers.PhoneNumberFormat.E164))
#             # countries_dict[country_code]["name"] + " " + phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164))
#         return {
#             "latitude": location.latitude,
#             "longitude": location.longitude,
#             "service_provider": service_provider
#         }
#     except:
#         return None
#
#
# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == "POST":
#         phone_number = request.form["phone_number"]
#         country_code = request.form["country_code"]
#         location_info = get_location_info(phone_number, country_code)
#         if location_info:
#             return render_template("info.html", phone_number=phone_number, location_info=location_info)
#         else:
#             return render_template("error.html", message="Invalid phone number")
#     else:
#         return render_template("index.html", countries=countries)
#
#
# @app.route("/map")
# def show_map():
#     phone_number = request.args.get("phone_number")
#     country_code = request.args.get("country_code")
#     location_info = get_location_info(phone_number, country_code)
#     if location_info:
#         map = folium.Map(location=[location_info["latitude"], location_info["longitude"]], zoom_start=10)
#         folium.Marker(location=[location_info["latitude"], location_info["longitude"]], popup=phone_number).add_to(map)
#         return map._repr_html_()
#     else:
#         return "Invalid phone number"
#
#
# if __name__ == '__main__':
#     # create a dictionary to map country codes to their details
#     # countries_dict = {country["code"]: country for country in countries}
#     app.run(debug=True)

# 3rd code

# # importing lib
# from flask import Flask, render_template, request, redirect, url_for
# import phonenumbers
# from geopy.geocoders import Nominatim
# import folium
# from phonenumbers import carrier
# import pycountry
#
# # app name
# app = Flask(__name__)
#
# # get list of all countries
# countries = list(pycountry.countries)
#
# def get_location_info(phone_number, country_code):
#     try:
#         parsed_number = phonenumbers.parse(phone_number, country_code)
#         service_provider = carrier.name_for_number(parsed_number, "en")
#         geolocator = Nominatim(user_agent="myapp")
#         location = geolocator.geocode(pycountry.countries.get(alpha_2=country_code).name + " " +
#                                       phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164))
#         return {
#             "latitude": location.latitude,
#             "longitude": location.longitude,
#             "service_provider": service_provider
#         }
#     except:
#         return None
#
#
# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == "POST":
#         phone_number = request.form["phone_number"]
#         country_code = request.form["country_code"]
#         location_info = get_location_info(phone_number, country_code)
#         if location_info:
#             return render_template("info.html", phone_number=phone_number, location_info=location_info)
#         else:
#             return render_template("error.html", message="Invalid phone number")
#     else:
#         return render_template("index.html", countries=countries)
#
#
# @app.route("/map")
# def show_map():
#     phone_number = request.args.get("phone_number")
#     country_code = request.args.get("country_code")
#     location_info = get_location_info(phone_number, country_code)
#     if location_info:
#         map = folium.Map(location=[location_info["latitude"], location_info["longitude"]], zoom_start=10)
#         folium.Marker(location=[location_info["latitude"], location_info["longitude"]], popup=phone_number).add_to(map)
#         return map._repr_html_()
#     else:
#         return "Invalid phone number"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
