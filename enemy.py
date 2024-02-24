from kivy.uix.image import Image
from kivy.animation import Animation, Sequence
import random, json
from kivy.event import EventDispatcher
from datetime import datetime
from kivy.clock import Clock

# 自作クラス
# from battle import BattleScreen

class EntryEnemy(Image, EventDispatcher):
    # 静的なカウンタを使用して一意のIDを生成
    enemy_id_counter =   0

    def __init__(self, json_data, **kwargs):
        super(EntryEnemy, self).__init__(**kwargs)
        # 敵が倒されるイベントを登録しておく
        self.register_event_type('on_enemy_defeated')
        self.register_event_type('on_enemy_generated')
        self.size = (50, 50)
        self.pop_up_flag = 0
        # jsonデータを辞書データに変換
        self.status = dict(json_data)
        # アニメーション動作秒数
        self.move_animation_time = 3
        # IDを割り当て
        self.id = EntryEnemy.enemy_id_counter
        EntryEnemy.enemy_id_counter +=   1

    def move_enemy_animation_fix(self):
        random_val = random.randint(-150, 150)
        anim_up = Animation(pos=(self.x, self.y + random_val), duration=self.move_animation_time)
        #  ウィジェットの初期位置から下に移動するアニメーションを作成
        anim_down = Animation(pos=(self.x, self.y), duration=self.move_animation_time)

        #  アニメーションを連鎖させ、最後に最初のアニメーションに戻るように設定
        self.anim = anim_up + anim_down
        # self.repeat = True
        self.anim.bind(on_complete=self.on_animation_complete)
        #  アニメーションを開始
        self.anim.start(self)
        self.anim.bind(on_progress=self.check_collision)

    def on_animation_complete(self, animation, instance):
        if self.pop_up_flag != 1:
            print("Animation completed:", datetime.now(), self.id)
            self.move_enemy_animation_fix()
        
    def check_collision(self, widget, progress, test):
        # ここでEnemyの位置を更新し、Playerとの衝突をチェックする
        self.x = self.pos[0]  # Enemyのx座標を更新
        self.y = self.pos[1]  # Enemyのy座標を更新
        if self.parent is not None and self.parent.player is not None:
            player = self.parent.player
            if self.collide_widget(player):
                # self.parent.stop_all_enemy_animations()
                self.show_battle_popup()

    def stop_animation(self):
        if self.anim:
            self.anim.stop(self)
            print('stoped:', self.id)

    def show_battle_popup(self):

        self.pop_up_flag = 1
        # アニメーションを停止する
        self.anim.stop(self)
        # self.anim.stop_all(self.parent)
        # 敵衝突をアンバインドする
        self.anim.unbind(on_progress=self.check_collision)
        self.anim.unbind(on_animation_complete=self.move_enemy_animation_fix)

        # ポップアップウィンドウを作成
        battle_screen = BattleScreen(self)
        battle_screen.open()
        
        battle_screen.bind(on_dismiss=self.resume_animation)
        
    def resume_animation(self, instance):
        print(self.enemy_id_counter)
        pass

    def on_enemy_defeated(self):
        self.enemy_id_counter -= 1
        print('敵が倒された')
        pass

    def on_enemy_generated(self):
        print(f'{self.enemy_name}が生成されました')
        pass

    def remove_enemy(self):
        # 敵を管理しているウィジェットから敵を削除する処理を実装
        if self.parent is not None:
            self.parent.remove_widget(self)
            # 敵が倒されたことを通知
            Clock.schedule_once(lambda dt: self.dispatch('on_enemy_defeated'), 10)

