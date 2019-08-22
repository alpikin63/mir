import requests
import json
from datetime import datetime


class Action(object):
    def __init__(self):
        self.BASE_URL = 'http://nspk.aeroidea.ru/api/'

    def get_actions(self, vesrion='v1', page='1', page_sise='100'):
        return json.loads(requests.get(
            url=self.BASE_URL+vesrion+'/promo-actions?page='+str(page)+'&pageSize='+str(page_sise)).text)

    def get_shop_groups(self, vesrion='v1', page='1', page_sise='100'):
        return json.loads(requests.get(
            url=self.BASE_URL + str(vesrion) + '/shop-groups?page=' + str(page) + '&pageSize=' + str(page_sise)).text)

    def get_city(self, vesrion='v1', page='1', page_sise='100'):
        return json.loads(requests.get(
            url=self.BASE_URL + vesrion + '/cities?page=' + str(page) + '&pageSize=' + str(page_sise)).text)

    def get_regions(self, vesrion='v1', page='1', page_sise='100'):
        return json.loads(requests.get(
            url=self.BASE_URL + vesrion + '/regions?page=' + str(page) + '&pageSize=' + str(page_sise)).text)

    def get_brands(self, vesrion='v1', page='1', page_sise='100'):
        return json.loads(requests.get(
            url=self.BASE_URL + vesrion + '/brands?page=' + str(page) + '&pageSize=' + str(page_sise)).text)

    def get_subway(self, vesrion='v1', page='1', page_sise='100'):
        return json.loads(requests.get(
            url=self.BASE_URL + vesrion + '/subway-stations?page=' + str(page) + '&pageSize=' + str(page_sise)).text)

    def get_shops(self, vesrion='v1', page='1', page_sise='100'):
        return json.loads(requests.get(
            url=self.BASE_URL + vesrion + '/shops?page=' + str(page) + '&pageSize=' + str(page_sise)).text)

    def all_actions(self):
        actoins = self.get_actions()['items']
        actoins_new = []
        if len(actoins) < 100:
            actoins_new = actoins
        else:
            pg = 1
            while (len(actoins) != 0):
                actoins = self.get_actions(page=str(pg))['items']
                if len(actoins) != 0:
                    actoins_new = actoins_new + actoins
                pg = pg + 1

        return actoins_new

    def all_shop_groups(self):
        actoins = self.get_shop_groups()['items']
        actoins_new = []
        if len(actoins) < 100:
            actoins_new = actoins
        else:
            pg = 1
            while (len(actoins) != 0):
                actoins = self.get_shop_groups(page=str(pg))['items']
                if len(actoins) != 0:
                    actoins_new = actoins_new + actoins
                pg = pg + 1

        return actoins_new

    def get_all_shops(self):
        actoins = self.get_shops()['items']
        actoins_new = []
        if len(actoins) < 100:
            actoins_new = actoins
        else:
            pg = 1
            while (len(actoins) != 0):
                actoins = self.get_shops(page=str(pg))['items']
                if len(actoins) != 0:
                    actoins_new = actoins_new + actoins
                pg = pg + 1

        return actoins_new

    def serach_active_actions(self):
        actoins = self.get_actions()['items']
        action_ids = []
        actoins_new = []
        data = datetime.now()
        if len(actoins) < 100:
            for action in actoins:
                end = datetime.strptime(action['endedAt'], '%Y-%m-%d')
                if data <= end:
                    action_ids.append({'id':action['id'], 'grops':action['joiningShopGroups']})
        else:
            pg = 1
            while(len(actoins)!=0):
                actoins = self.get_actions(page=str(pg))['items']
                if len(actoins) != 0:
                    actoins_new = actoins_new + actoins
                pg = pg+1

            for action in actoins_new:
                end = datetime.strptime(action['endedAt'], '%Y-%m-%d')
                if data <= end:
                    action_ids.append({'id':action['id'], 'groups': action['joiningShopGroups']})
        return action_ids

    def get_actions_shop_groups(self, action_id):
        actions = self.all_actions()
        shopgr = []
        for action in actions:
            if action['id'] == action_id:
                for groups in action['joiningShopGroups']:
                    shopgr.append(groups['shopGroupId'])
        return shopgr

    def get_actions_regions(self, action_id):
        shop_gr = self.get_actions_shop_groups(action_id=action_id)
        regions = []
        for gr in shop_gr:
            gr_reg = self.get_shopgroups_regions(gr)
            regions = regions + gr_reg
        return regions

    def get_shopgroups_regions(self, shopgr_id):
        groups = self.all_shop_groups()
        group = []
        regions_online = []
        regions_ofline = []
        for gr in groups:
            if gr['id'] == shopgr_id:
                group = gr

        if 'online' in group['type']:
            regions_online = group['regionId']

        if 'offline' in group['type']:
            shops = self.get_all_shops()
            for shop in shops:
                if shop['shopGroupId'] == shopgr_id:
                    regions_ofline.append(shop['regionId'])

        return list(set(regions_ofline + regions_online))

    def get_region_by_id(self, reg_id):
        regions = self.get_regions()['items']
        reg_name = ''
        for region in regions:
            if str(region['id']) == str(reg_id):
                reg_name = region['name']
        return reg_name
