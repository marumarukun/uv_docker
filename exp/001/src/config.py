import os
import sys

from hydra import compose, initialize_config_dir


class Config:
    """
    hydraによる設定値の取得 (conf)
    """

    @staticmethod
    def get_cfg():
        """
        設定値の辞書を取得
        @return
            cnf: OmegaDict
        """
        # このファイル（config.py）のディレクトリを取得
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # プロジェクトのルートディレクトリ（current_dirの親）を取得
        project_root = os.path.dirname(current_dir)

        # confディレクトリのパスを構築
        conf_dir = os.path.join(project_root, "config")

        if not os.path.isdir(conf_dir):
            print(f"Can not find directory: {conf_dir}.")
            sys.exit(-1)

        with initialize_config_dir(version_base=None, config_dir=conf_dir):
            cfg = compose(config_name="config")
            return cfg


cfg = Config.get_cfg()
