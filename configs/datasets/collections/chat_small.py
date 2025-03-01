from mmengine.config import read_base

with read_base():
    from ..mmlu.mmlu_gen_a484b3 import mmlu_datasets
    from ..ceval.ceval_gen_5f30c7 import ceval_datasets
    from ..bbh.bbh_gen_6bd693 import bbh_datasets
    from ..CLUE_CMRC.CLUE_CMRC_gen_1bd3c8 import CMRC_datasets
    from ..CLUE_DRCD.CLUE_DRCD_gen_1bd3c8 import DRCD_datasets
    from ..CLUE_afqmc.CLUE_afqmc_gen_901306 import afqmc_datasets
    from ..FewCLUE_bustm.FewCLUE_bustm_gen_634f41 import bustm_datasets
    from ..FewCLUE_chid.FewCLUE_chid_gen_0a29a2 import chid_datasets
    from ..FewCLUE_cluewsc.FewCLUE_cluewsc_gen_c68933 import cluewsc_datasets
    from ..FewCLUE_eprstmt.FewCLUE_eprstmt_gen_740ea0 import eprstmt_datasets
    from ..humaneval.humaneval_gen_8e312c import humaneval_datasets
    from ..mbpp.mbpp_gen_1e1056 import mbpp_datasets
    from ..lambada.lambada_gen_217e11 import lambada_datasets
    from ..storycloze.storycloze_gen_7f656a import storycloze_datasets
    from ..SuperGLUE_AX_b.SuperGLUE_AX_b_gen_4dfefa import AX_b_datasets
    from ..SuperGLUE_AX_g.SuperGLUE_AX_g_gen_68aac7 import AX_g_datasets
    from ..SuperGLUE_BoolQ.SuperGLUE_BoolQ_gen_883d50 import BoolQ_datasets
    from ..SuperGLUE_CB.SuperGLUE_CB_gen_854c6c import CB_datasets
    from ..SuperGLUE_COPA.SuperGLUE_COPA_gen_91ca53 import COPA_datasets
    from ..SuperGLUE_MultiRC.SuperGLUE_MultiRC_gen_27071f import MultiRC_datasets
    from ..SuperGLUE_RTE.SuperGLUE_RTE_gen_68aac7 import RTE_datasets
    from ..SuperGLUE_ReCoRD.SuperGLUE_ReCoRD_gen_30dea0 import ReCoRD_datasets
    from ..SuperGLUE_WiC.SuperGLUE_WiC_gen_d06864 import WiC_datasets
    from ..SuperGLUE_WSC.SuperGLUE_WSC_gen_8a881c import WSC_datasets
    from ..race.race_gen_69ee4f import race_datasets
    from ..math.math_gen_265cce import math_datasets
    from ..gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets
    from ..summedits.summedits_gen_315438 import summedits_datasets
    from ..hellaswag.hellaswag_gen_6faab5 import hellaswag_datasets
    from ..piqa.piqa_gen_1194eb import piqa_datasets
    from ..winogrande.winogrande_gen_a9ede5 import winogrande_datasets
    from ..obqa.obqa_gen_9069e4 import obqa_datasets
    from ..nq.nq_gen_c788f6 import nq_datasets
    from ..triviaqa.triviaqa_gen_2121ce import triviaqa_datasets
    from ..crowspairs.crowspairs_gen_381af0 import crowspairs_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
