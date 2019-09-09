##Docs: https://docs.python-guide.org/scenarios/scrape/
#http://docs.python-requests.org/en/master/api/#requests.Response
#https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3

from lxml import html
import requests
import json

#import urllib.request
#page = urllib.request.urlopen('https://pin.it/yzfyofnadh6n4g')
page = requests.get('https://pin.it/yzfyofnadh6n4g')
tree = html.fromstring(page.content)
json_pins = tree.xpath('//script[@id="initial-state"]/text()')
pins = json.loads(json_pins[0])
#data_pins = pin["pins"]
pathname = pins["location"]["pathname"].split('/') # "/pin/459085755761840151/sent/?sfo=1&sender=259660872174066757&invite_code=4155b0f3858748c3abc79ab707d87c93"
id_pin = pathname[2]
print(pins["pins"][id_pin]['images']['orig'])
#print(pins["resources"]["data"]["PinResource"]['data']['images'])
#pin = page.html.find('#initial-state', first=True)
#print(pin)
#print(page.read())

#https://i.pinimg.com/originals/e7/1f/0c/e71f0ceadb3f368854f0576fcc3836b8.png
#
#
#
#
'''[summary]

{
	"euCookieBar": {
		"isShowEUCookieBar": false
	},
	"inviteObject": {
		"loadedState": "Unloaded",
		"invite": {}
	},
	"googleOneTap": {
		"googleOneTapFail": false
	},
	"boards": {
		"content": {},
		"fetching": {},
		"deleting": {},
		"fetchAllComplete": false,
		"lastPinnedTo": null
	},
	"facebookAutoLogin": {
		"facebookAutoLoginStatus": "unknown"
	},
	"viewer": {
		"isLimitedLogin": false,
		"isAuth": false
	},
	"giftWrapperPinType": {
		"pinType": "DEFAULT"
	},
	"brandAboutPage": {
		"showBrandAboutPage": false
	},
	"experiences": {
		"eligibleExperiences": {},
		"mountedPlacements": {},
		"isFetchingAll": false,
		"anchorExperiences": {}
	},
	"location": {
		"pathname": "/pin/459085755761840151/sent/?sfo=1&sender=259660872174066757&invite_code=4155b0f3858748c3abc79ab707d87c93",
		"history": [{
			"pathname": "/pin/459085755761840151/sent/?sfo=1&sender=259660872174066757&invite_code=4155b0f3858748c3abc79ab707d87c93"
		}]
	},
	"loggedOutUserInfo": {
		"userInfo": {}
	},
	"pins": {
		"459085755761840151": {
			"origin_pinner": null,
			"domain": "watabou.itch.io",
			"videos": null,
			"image_signature": "e71f0ceadb3f368854f0576fcc3836b8",
			"images": {
				"170x": {
					"url": "https://i.pinimg.com/170x/e7/1f/0c/e71f0ceadb3f368854f0576fcc3836b8.jpg",
					"width": 170,
					"height": 170
				},
				"474x": {
					"url": "https://i.pinimg.com/474x/e7/1f/0c/e71f0ceadb3f368854f0576fcc3836b8.jpg",
					"width": 474,
					"height": 474
				},
				"orig": {
					"url": "https://i.pinimg.com/originals/e7/1f/0c/e71f0ceadb3f368854f0576fcc3836b8.png",
					"width": 794,
					"height": 794
				},
				"236x": {
					"url": "https://i.pinimg.com/236x/e7/1f/0c/e71f0ceadb3f368854f0576fcc3836b8.jpg",
					"width": 236,
					"height": 236
				}
			},
			"id": "459085755761840151",
			"category": "art",
			"description_html": "Medieval Fantasy City Generator by watabou",
			"title": "",
			"buyable_product": null,
			"board": {
				"url": "/alphabetsun/d-d-bitches/",
				"name": "D & D, Bitches",
				"image_thumbnail_url": "https://i.pinimg.com/upload/459085824454675256_board_thumbnail_2019-03-12-23-29-18_14696_60.jpg"
			},
			"link_domain": {
				"official_user": null
			},
			"description": "Medieval Fantasy City Generator by watabou",
			"last_repin_date": "Wed, 19 Sep 2018 23:44:59 +0000",
			"rich_metadata": null,
			"tracking_params_map": {},
			"link": "https://watabou.itch.io/medieval-fantasy-city-generator",
			"pinner": {
				"username": "alphabetsun",
				"image_small_url": "https://i.pinimg.com/30x30_RS/c7/14/39/c7143921a23b202769a52b6b53c79a05.jpg",
				"full_name": "Rae"
			},
			"repin_count": 1,
			"tracked_link": "https://watabou.itch.io/medieval-fantasy-city-generator",
			"created_at": "Fri, 07 Sep 2018 19:00:43 +0000",
			"dominant_color": "#fff2c8",
			"pin_join": {
				"canonical_pin": {
					"id": "459085755761840151"
				},
				"visual_descriptions": [],
				"seo_description": "Medieval Fantasy City Generator by watabou",
				"visual_annotation": ["Fantasy Town", "Medieval Fantasy", "City Generator", "Writing Inspiration", "Art Reference", "Building Ideas", "Knight", "Blood", "Fantasy City"],
				"annotations_with_links": {
					"Fantasy City": {
						"url": "/artemisraethron/fantasy-city/",
						"name": "Fantasy City"
					},
					"Art Reference": {
						"url": "/topics/art-reference/",
						"name": "Art Reference"
					},
					"Medieval Fantasy": {
						"url": "/ckiwi98/medieval-fantasy/",
						"name": "Medieval Fantasy"
					},
					"Building Ideas": {
						"url": "/jorylee76/building-ideas/",
						"name": "Building Ideas"
					},
					"Writing Inspiration": {
						"url": "/topics/writing-inspiration/",
						"name": "Writing Inspiration"
					},
					"City Generator": {
						"url": "/neum728/city-generator/",
						"name": "City Generator"
					},
					"Blood": {
						"url": "/topics/blood/",
						"name": "Blood"
					},
					"Fantasy Town": {
						"url": "/Reymort/fantasy-town/",
						"name": "Fantasy Town"
					},
					"Knight": {
						"url": "/pablomesavera/knight/",
						"name": "Knight"
					}
				}
			},
			"embed": null,
			"closeup_description": null
		}
	},
	"ui": {
		"conversations": {
			"chatheads": [],
			"open": null,
			"feedback": null
		},
		"visualLinks": {
			"selectedPinTagKey": null
		},
		"mainComponent": {
			"current": "StaticRouteData(WithUnauthSeoExperiments(Connect(PinFeedbackPageContainer)))",
			"initial": "StaticRouteData(WithUnauthSeoExperiments(Connect(PinFeedbackPageContainer)))",
			"locationToErrorMap": {},
			"upwtActionName": null
		},
		"homefeed": {
			"prefetchBookmark": ""
		},
		"toasts": [],
		"login": {
			"showModal": false
		},
		"gdprModal": {
			"showParentConsentModal": false,
			"showModal": false
		}
	},
	"boardSort": {
		"sort": "popular"
	},
	"resources": {
		"fetching": {},
		"data": {
			"UserResource": {
				"user_id=\\"
				259660872174066757\\ "": {
					"nextBookmark": "-end-",
					"data": {
						"show_creator_profile": false,
						"impressum_url": null,
						"last_name": "",
						"domain_verified": false,
						"following_count": 255,
						"profile_reach": -1,
						"image_medium_url": "https://s.pinimg.com/images/user/default_75.png",
						"story_pin_count": 0,
						"image_xlarge_url": "https://s.pinimg.com/images/user/default_280.png",
						"full_name": "Pablo",
						"profile_discovered_public": null,
						"image_small_url": "https://s.pinimg.com/images/user/default_30.png",
						"id": "259660872174066757",
						"first_name": "Pablo",
						"domain_url": null,
						"has_shopping_showcase": false,
						"explicitly_followed_by_me": false,
						"location": "",
						"indexed": false,
						"is_tastemaker": false,
						"type": "user",
						"profile_cover_source": null,
						"website_url": null,
						"board_count": 20,
						"username": "Bay122pj",
						"verified_identity": {},
						"has_showcase": false,
						"last_pin_save_time": "Wed, 13 Mar 2019 11:48:30 +0000",
						"follower_count": 74,
						"is_partner": false,
						"pins_done_count": 0,
						"has_custom_board_sorting_order": false,
						"pin_count": 3727,
						"native_pin_count": 0,
						"about": "",
						"show_discovered_feed": null,
						"show_impressum": false,
						"joined_communities_count": 0,
						"image_large_url": "https://s.pinimg.com/images/user/default_140.png",
						"blocked_by_me": false
					},
					"options": {
						"user_id": "259660872174066757"
					},
					"prefetchHasBeenRead": false,
					"isPrefetch": false
				}
			},
			"PinResource": {
				"field_set_key=\\"
				detailed\\ ",id=\\"
				459085755761840151\\ ",skip_page_metadata=true": {
					"nextBookmark": "-end-",
					"error": null,
					"data": {
						"origin_pinner": null,
						"domain": "watabou.itch.io",
						"videos": null,
						"image_signature": "e71f0ceadb3f368854f0576fcc3836b8",
						"images": {
							"170x": {
								"url": "https://i.pinimg.com/170x/e7/1f/0c/e71f0ceadb3f368854f0576fcc3836b8.jpg",
								"width": 170,
								"height": 170
							},
							"474x": {
								"url": "https://i.pinimg.com/474x/e7/1f/0c/e71f0ceadb3f368854f0576fcc3836b8.jpg",
								"width": 474,
								"height": 474
							},
							"orig": {
								"url": "https://i.pinimg.com/originals/e7/1f/0c/e71f0ceadb3f368854f0576fcc3836b8.png",
								"width": 794,
								"height": 794
							},
							"236x": {
								"url": "https://i.pinimg.com/236x/e7/1f/0c/e71f0ceadb3f368854f0576fcc3836b8.jpg",
								"width": 236,
								"height": 236
							}
						},
						"id": "459085755761840151",
						"category": "art",
						"description_html": "Medieval Fantasy City Generator by watabou",
						"title": "",
						"buyable_product": null,
						"board": {
							"url": "/alphabetsun/d-d-bitches/",
							"name": "D & D, Bitches",
							"image_thumbnail_url": "https://i.pinimg.com/upload/459085824454675256_board_thumbnail_2019-03-12-23-29-18_14696_60.jpg"
						},
						"link_domain": {
							"official_user": null
						},
						"description": "Medieval Fantasy City Generator by watabou",
						"last_repin_date": "Wed, 19 Sep 2018 23:44:59 +0000",
						"rich_metadata": null,
						"tracking_params_map": {},
						"link": "https://watabou.itch.io/medieval-fantasy-city-generator",
						"pinner": {
							"username": "alphabetsun",
							"image_small_url": "https://i.pinimg.com/30x30_RS/c7/14/39/c7143921a23b202769a52b6b53c79a05.jpg",
							"full_name": "Rae"
						},
						"repin_count": 1,
						"tracked_link": "https://watabou.itch.io/medieval-fantasy-city-generator",
						"created_at": "Fri, 07 Sep 2018 19:00:43 +0000",
						"dominant_color": "#fff2c8",
						"pin_join": {
							"canonical_pin": {
								"id": "459085755761840151"
							},
							"visual_descriptions": [],
							"seo_description": "Medieval Fantasy City Generator by watabou",
							"visual_annotation": ["Fantasy Town", "Medieval Fantasy", "City Generator", "Writing Inspiration", "Art Reference", "Building Ideas", "Knight", "Blood", "Fantasy City"],
							"annotations_with_links": {
								"Fantasy City": {
									"url": "/artemisraethron/fantasy-city/",
									"name": "Fantasy City"
								},
								"Art Reference": {
									"url": "/topics/art-reference/",
									"name": "Art Reference"
								},
								"Medieval Fantasy": {
									"url": "/ckiwi98/medieval-fantasy/",
									"name": "Medieval Fantasy"
								},
								"Building Ideas": {
									"url": "/jorylee76/building-ideas/",
									"name": "Building Ideas"
								},
								"Writing Inspiration": {
									"url": "/topics/writing-inspiration/",
									"name": "Writing Inspiration"
								},
								"City Generator": {
									"url": "/neum728/city-generator/",
									"name": "City Generator"
								},
								"Blood": {
									"url": "/topics/blood/",
									"name": "Blood"
								},
								"Fantasy Town": {
									"url": "/Reymort/fantasy-town/",
									"name": "Fantasy Town"
								},
								"Knight": {
									"url": "/pablomesavera/knight/",
									"name": "Knight"
								}
							}
						},
						"embed": null,
						"closeup_description": null
					},
					"options": {
						"field_set_key": "detailed",
						"skip_page_metadata": true,
						"id": "459085755761840151"
					},
					"prefetchHasBeenRead": false,
					"isPrefetch": false
				}
			}
		}
	},
	"history": {
		"current": null,
		"forward": [],
		"previous": []
	}
}

[description]
'''