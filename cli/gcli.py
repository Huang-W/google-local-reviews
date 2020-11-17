import argparse
from math import sin, cos, sqrt, atan2, radians
from operator import itemgetter

import pandas as pd

from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

feature_names = ['abbey', 'accessories', 'accommodation', 'accountant', 'accounting', 'activity', 'adult', 'afghani', 'african', 'agency', 'agricultural', 'agriculture', 'airbrushing', 'aircraft', 'airport', 'alley', 'alsace', 'alternative', 'ambulance', 'american', 'amish', 'amusement', 'angler', 'animals', 'antique', 'apartment', 'apparel', 'appliance', 'appraiser', 'aquarium', 'arcade', 'archery', 'architect', 'area', 'argentinian', 'armenian', 'army', 'aromatherapy', 'art', 'artist', 'arts', 'asian', 'assisted', 'association', 'athletic', 'atm', 'attorney', 'attraction', 'auditorium', 'australian', 'austrian', 'authentic', 'auto', 'baby', 'bagel', 'bait', 'baked', 'bakery', 'baking', 'ball', 'ballet', 'balloon', 'ballroom', 'band', 'bangladeshi', 'bank', 'banking', 'banquet', 'bar', 'barbecue', 'barber', 'barn', 'bartending', 'base', 'baseball', 'basket', 'basketball', 'basque', 'bathroom', 'battery', 'batting', 'beach', 'bead', 'beauty', 'bed', 'beer', 'belgian', 'betting', 'beverage', 'beverages', 'bicycle', 'bicycles', 'billiards', 'bingo', 'bistro', 'blower', 'blues', 'boarding', 'boat', 'bocce', 'body', 'book', 'boot', 'botanical', 'bottled', 'boutique', 'bowling', 'box', 'boys', 'brake', 'brasserie', 'brazilian', 'breakfast', 'brewery', 'brewing', 'brewpub', 'bridal', 'british', 'brunch', 'bubble', 'buddhist', 'buffet', 'builder', 'building', 'bulgarian', 'bureau', 'burmese', 'burrito', 'bus', 'business', 'butcher', 'cabin', 'cabinet', 'cafe', 'cage', 'cajun', 'cake', 'californian', 'calvary', 'cambodian', 'camp', 'campground', 'camping', 'campus', 'canadian', 'candle', 'candy', 'canoe', 'cantonese', 'car', 'card', 'care', 'caribbean', 'carpet', 'cart', 'cashing', 'casino', 'catalonian', 'caterer', 'catering', 'cave', 'cd', 'cell', 'center', 'central', 'change', 'chapel', 'charging', 'charity', 'charter', 'check', 'cheese', 'cheesesteak', 'chicken', 'child', 'children', 'chilean', 'chinaware', 'chinese', 'chips', 'chiropractor', 'chocolate', 'chophouse', 'christian', 'church', 'cider', 'cigar', 'cigarette', 'circus', 'city', 'cleaner', 'cleaning', 'clinic', 'clothing', 'club', 'cocktail', 'coffee', 'coin', 'collectibles', 'college', 'colombian', 'comedy', 'comic', 'commerce', 'community', 'company', 'complex', 'computer', 'concert', 'condiments', 'condominium', 'conference', 'consignment', 'construction', 'consultant', 'contemporary', 'continental', 'contractor', 'convenience', 'convention', 'cookie', 'cooking', 'cooperative', 'corporate', 'cosmetics', 'costa', 'costume', 'cottage', 'countertop', 'country', 'courier', 'course', 'court', 'crab', 'craft', 'cream', 'creole', 'croatian', 'cruise', 'crêperie', 'cuban', 'culinary', 'cultural', 'culture', 'cupcake', 'currency', 'curry', 'custom', 'czech', 'dairy', 'dance', 'danish', 'dart', 'davidson', 'day', 'dealer', 'deli', 'delivery', 'denominational', 'dentist', 'department', 'desert', 'designer', 'dessert', 'detailing', 'development', 'diesel', 'dim', 'diner', 'dining', 'dinner', 'discotheque', 'discount', 'distributor', 'dive', 'dj', 'dock', 'dog', 'doll', 'dollar', 'dominican', 'donut', 'drama', 'dressmaker', 'dried', 'drink', 'drive', 'driving', 'dry', 'dumpling', 'duplication', 'dutch', 'dvd', 'east', 'eastern', 'eatery', 'eclectic', 'ecuadorian', 'education', 'egyptian', 'electric', 'electrician', 'electronics', 'england', 'english', 'entertainer', 'entertainment', 'equipment', 'escrow', 'espresso', 'estate', 'ethiopian', 'ethnic', 'european', 'event', 'exchange', 'executive', 'exercise', 'extended', 'eye', 'facility', 'factory', 'fairground', 'falafel', 'family', 'farm', 'farmers', 'fashion', 'fast', 'fax', 'feature', 'feed', 'ferry', 'fertilizer', 'fi', 'field', 'filipino', 'finance', 'financial', 'fine', 'fire', 'fireplace', 'firewood', 'fish', 'fishing', 'fitness', 'flea', 'floridian', 'florist', 'flower', 'fondue', 'food', 'foods', 'football', 'fraternal', 'free', 'french', 'frozen', 'fruit', 'fuel', 'function', 'furniture', 'fusion', 'gallery', 'game', 'garage', 'garden', 'gas', 'gastropub', 'gay', 'general', 'german', 'ghost', 'gift', 'glass', 'gluten', 'go', 'golf', 'goods', 'gospel', 'gourmet', 'government', 'graphic', 'greek', 'greengrocer', 'greenhouse', 'greeting', 'grill', 'grocer', 'grocery', 'groomer', 'ground', 'group', 'guatemalan', 'guest', 'guitar', 'gun', 'gym', 'gyro', 'hair', 'haitian', 'halal', 'hall', 'ham', 'hamburger', 'harbor', 'hardware', 'harley', 'haunted', 'hawaiian', 'headquarters', 'health', 'heliport', 'herb', 'high', 'higher', 'historical', 'history', 'hoagie', 'hobby', 'hockey', 'holistic', 'home', 'honduran', 'hookah', 'horseback', 'hostel', 'hot', 'hotel', 'house', 'hunan', 'hungarian', 'ice', 'importer', 'indian', 'indonesian', 'indoor', 'information', 'inn', 'inspection', 'instructor', 'instrument', 'insurance', 'interior', 'internet', 'internist', 'irish', 'israeli', 'italian', 'izakaya', 'jamaican', 'japanese', 'jazz', 'jeweler', 'jewelry', 'jewish', 'juice', 'kaiseki', 'karaoke', 'kart', 'kayak', 'kerosene', 'key', 'kindergarten', 'kitchen', 'korean', 'kosher', 'lab', 'lake', 'landmark', 'landscape', 'landscaping', 'lankan', 'laotian', 'laser', 'latin', 'latino', 'laundromat', 'laundry', 'lawn', 'learning', 'lebanese', 'lesbian', 'library', 'lighthouse', 'lighting', 'limousine', 'line', 'liquor', 'lithuanian', 'live', 'living', 'loan', 'lobster', 'locality', 'location', 'lodge', 'lodging', 'loss', 'lot', 'lottery', 'louisiana', 'lounge', 'luggage', 'lunch', 'luxury', 'machine', 'magazine', 'magician', 'mailing', 'maintenance', 'malaysian', 'mall', 'management', 'mandarin', 'manufacturer', 'manufacturing', 'marina', 'marine', 'marines', 'market', 'marketing', 'massage', 'meat', 'medicine', 'mediterranean', 'meeting', 'men', 'methodist', 'mex', 'mexican', 'middle', 'milk', 'mill', 'miniature', 'miniatures', 'mining', 'mobile', 'modern', 'monastery', 'money', 'mongolian', 'moroccan', 'motel', 'motor', 'motorcycle', 'movie', 'moving', 'museum', 'music', 'musical', 'musician', 'nail', 'national', 'native', 'natural', 'navy', 'nazarene', 'neapolitan', 'nepalese', 'new', 'news', 'newspaper', 'newsstand', 'nicaraguan', 'night', 'nightlife', 'non', 'noodle', 'north', 'northern', 'northwest', 'norwegian', 'novelties', 'nudist', 'nuevo', 'nursery', 'nut', 'nutritionist', 'observatory', 'office', 'oil', 'okonomiyaki', 'opera', 'operated', 'optician', 'optometrist', 'orchard', 'order', 'organic', 'organization', 'orthopedic', 'outdoor', 'outfitter', 'outlet', 'oyster', 'pacific', 'packer', 'paintball', 'pakistani', 'pan', 'pancake', 'pantry', 'park', 'parking', 'parts', 'party', 'pasta', 'pastry', 'patch', 'patisserie', 'pennsylvania', 'performing', 'persian', 'personal', 'peruvian', 'pet', 'pharmacy', 'pho', 'phone', 'photo', 'photographer', 'physical', 'physician', 'piano', 'picnic', 'pie', 'pier', 'piercing', 'pizza', 'place', 'planner', 'planning', 'plant', 'plastic', 'plates', 'playground', 'po', 'police', 'polish', 'polynesian', 'pool', 'popcorn', 'portuguese', 'post', 'pottery', 'poultry', 'practitioner', 'preparation', 'pretzel', 'print', 'printer', 'private', 'processor', 'produce', 'products', 'professional', 'profit', 'program', 'propane', 'property', 'provence', 'provider', 'psychic', 'pub', 'public', 'publisher', 'puerto', 'pump', 'pumpkin', 'québécois', 'racing', 'rack', 'raft', 'ramen', 'ranch', 'range', 'rare', 'raw', 'real', 'record', 'recording', 'recreation', 'religious', 'removal', 'rental', 'repair', 'reservation', 'resort', 'rest', 'restoration', 'retailer', 'retreat', 'rican', 'riding', 'rim', 'rink', 'river', 'roller', 'roman', 'romanian', 'room', 'rugby', 'russian', 'rustic', 'rv', 'salad', 'salon', 'salvadoran', 'sandwich', 'sandwiches', 'scaffolding', 'scandinavian', 'school', 'screen', 'scuba', 'sculpture', 'seafood', 'seaplane', 'seating', 'self', 'serbian', 'service', 'services', 'sewing', 'shabu', 'shanghainese', 'shipping', 'shipyard', 'shirt', 'shoe', 'shop', 'shopping', 'shuttle', 'sichuan', 'sicilian', 'sightseeing', 'sign', 'singaporean', 'singing', 'skateboard', 'skating', 'ski', 'small', 'smog', 'snack', 'snowboard', 'soba', 'soccer', 'social', 'softball', 'soul', 'soup', 'south', 'southeast', 'southern', 'southwestern', 'souvenir', 'spa', 'space', 'spanish', 'spice', 'sporting', 'sports', 'sportswear', 'spot', 'spring', 'sprinkler', 'sri', 'stage', 'stand', 'state', 'station', 'stationery', 'stay', 'steak', 'steakhouse', 'steakhouses', 'stop', 'storage', 'store', 'stores', 'stove', 'strip', 'studio', 'subway', 'suite', 'sukiyaki', 'sum', 'sunglasses', 'supermarket', 'supplements', 'supplier', 'supply', 'surf', 'surgeon', 'sushi', 'swedish', 'swim', 'swimming', 'swiss', 'syrian', 'system', 'table', 'taco', 'tag', 'tailor', 'taiwanese', 'takeout', 'talent', 'tamale', 'tanning', 'tapas', 'tattoo', 'tax', 'tea', 'telegram', 'television', 'temple', 'tempura', 'tennis', 'teppanyaki', 'tex', 'thai', 'theater', 'theme', 'therapist', 'therapy', 'thrift', 'tile', 'tire', 'tobacco', 'tonkatsu', 'tour', 'tourist', 'town', 'toy', 'toyota', 'track', 'trade', 'trading', 'traditional', 'train', 'trainer', 'transfer', 'translator', 'transport', 'travel', 'trip', 'truck', 'trucking', 'tunisian', 'turkish', 'tuscan', 'tutoring', 'ukrainian', 'united', 'university', 'uruguayan', 'us', 'used', 'uzbeki', 'vacation', 'vacuum', 'variety', 'vegan', 'vegetable', 'vegetarian', 'vehicle', 'vending', 'venetian', 'venezuelan', 'venue', 'veterans', 'veterinarian', 'video', 'vietnamese', 'vineyard', 'vintage', 'vitamin', 'volleyball', 'volunteer', 'warehouse', 'wash', 'water', 'wedding', 'weddings', 'weight', 'wellness', 'west', 'western', 'wheel', 'wholesale', 'wholesaler', 'wi', 'window', 'wine', 'winemaking', 'winery', 'wings', 'women', 'wood', 'wrap', 'wrecker', 'yacht', 'yakitori', 'yarn', 'yoga', 'yogurt', 'youth', 'zealand']

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def calculate_distance(lat1, lon1, lat2, lon2):
    """Helper function to calculate distance between two cordinates"""
    # approximate radius of earth in km
    R = 6373.0

    lat1_r = radians(lat1)
    lon1_r = radians(lon1)
    lat2_r = radians(lat1)
    lon2_r = radians(lon2)

    dlon = lon2_r - lon1_r
    dlat = lat2_r - lat1_r

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

#  defining the function that takes in places
# as input and returns the top 10 recommendations based on content and distance
def recommendations_content_distance(df,
                                     src_lat,
                                     src_lon,
                                     features,
                                     distance_limit=10,
                                     desired_similarity=0.5):
    # initializing the empty list of recommended places
    recommended_places = []

    sim_vector = [[1 if f in features else 0 for f in feature_names]]

    #Calculate cosine similarity
    cosine_sim = cosine_similarity(sim_vector, count_matrix)
    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[0]).sort_values(ascending = False)
    # Filtering the similar placees based on distance to find
    # top recommendations

    counter = 0 # UpTo 10  for 10 recommendations to optimize the loop
    for score_i, score_v in score_series.items():
        try:
            dest_lat = df['place_lat'].iloc[score_i]
            dest_lon = df['place_long'].iloc[score_i]
            dis = calculate_distance(src_lat, src_lon, dest_lat, dest_lon)
            if dis<=distance_limit and dis>0 and score_v>=desired_similarity:
                place_name = df['placeName'].iloc[score_i]
                place_category = df['categories'].iloc[score_i]
                addr = df['address'].iloc[score_i]
                price = df['price'].iloc[score_i]
                recommended_places.append({'Place':place_name,
                                           'Address': addr,
                                           'Distance(km)': dis,
                                           'Price': price})
                counter+=1

            if counter == 10:
                break
        except Exception as e:
            pass
    return sorted(recommended_places, key=itemgetter('Distance(km)'))

if __name__ == '__main__':

    category_choices = ['european', 'asian', 'american', 'italian', 'bar', 'pizza',
    'fast food', 'cafe', 'chinese', 'mexican', 'latin american', 'seafood', 'hamburger', 'coffee shop',
    'japanese', 'pub', 'bar & grill', 'steak house', 'sandwich shop', 'bakery', 'barbecue', 'sushi',
    'french', 'indian', 'southeast asian', 'south asian', 'dessert shop',
    'mediterranean', 'takeout', 'deli', 'thai', 'ice cream shop']

    parser = argparse.ArgumentParser(description=f'Try out these categories: {category_choices}')

    parser.add_argument('--location',
        nargs=1,
        required=True,
        help='Either enter a location: e.g. "San Jose, CA" or enter longitude, latitude coordinates: e.g. "-76.23, 123"')
    parser.add_argument('--distance',
        nargs=1,
        type=int,
        default=10,
        help='Recommendations will remain with the maximum distance from selected location. Default to 10km')
    parser.add_argument('--categories',
        nargs='+',
        required=True,
        help='Decide on your categories of restaurants')

    args = parser.parse_args()
    # print(args)

    categories=args.categories
    distance=args.distance
    location=tuple(map(str.strip, args.location[0].split(',')))
    # print(categories,distance,location)

    # 200 ms
    count_matrix = sparse.load_npz('cli/count_matrix.npz')

    # convert city, state to lat, long (if needed)
    us_cities = pd.read_csv('cli/us_cities.csv')
    lat = long = None
    if all(map(is_number, location)):
        lat, long = float(location[0]), float(location[1])
    else:
        city, state = location[0], location[1]
        row = us_cities.loc[(us_cities['CITY'] == city) & (us_cities['STATE_CODE'] == state)][['LATITUDE', 'LONGITUDE']]
        if len(row) != 1:
            print('City, State not found. Unable to make recommendation.')
            exit()
        lat, long = row['LATITUDE'].values[0], row['LONGITUDE'].values[0]

    # 5 seconds
    usa_df = pd.read_csv('cli/usa_df_content.csv')

    places_rec = recommendations_content_distance(usa_df, lat, long, categories, distance, 0.5)

    print('Listing restaurants...\n\n')

    # list top 3 by distance
    for i in range(3):
        obj = places_rec[i]
        print(f'Restaurant Name: {obj["Place"]}')
        print(f'Address:         {" ".join(eval(obj["Address"]))}')
        print(f'Distance(km):    {obj["Distance(km)"]}')
        print(f'Price Range:     {obj["Price"]}\n')