import axios from 'axios';
import * as TYPES from './types';
import helper from '../helper';

export default {
  state: {
    all: [],
    report: {},
    themes: [],
  },

  getters: {
    getReports: state => state.all,
    getReport: state => state.report,
  },

  /* eslint-disable no-param-reassign */
  mutations: {
    [TYPES.SET_REPORTS](state, obj) {
      state.all = obj;
    },

    [TYPES.SET_CURRENT_REPORT](state, obj) {
      state.theme = obj;
    },

    [TYPES.ADD_REPORTS_LIST](state, obj) {
      if (state.themes.length === 0) {
        state.all = [];
        state.all = obj.data;
      } else {
        Object.keys(obj.data).map((key, index) => {
          state.all.push(obj.data[index]);
          return true;
        });
      }

      state.themes.push(obj.theme);
    },

    [TYPES.REMOVE_REPORTS_LIST](state, obj) {
      const index = state.themes.indexOf(obj.theme);
      if (index !== -1) {
        console.log('REMOVE');
        state.themes.splice(index, 1);
        const aa = state.all.filter((cc) => {
          console.log(cc);
          return cc;
        });
        console.log(aa);
      }
    },
  },

  actions: {
    getReports({ commit }) {
      const project = helper.getItem('project');
      axios.get(`/api/reports?project=${project.id}`).then((response) => {
        commit(TYPES.SET_REPORTS, response.data);
      }).catch((error) => {
        throw new Error(error);
      });
    },

    getReportsByTheme({ commit }, obj) {
      if (obj.isChecked) {
        axios.get(`/api/reports?theme=${obj.themeId}`).then((response) => {
          commit(TYPES.ADD_REPORTS_LIST, {
            data: response.data,
            theme: obj.themeId,
          });
        }).catch((error) => {
          throw new Error(error);
        });
      } else {
        commit(TYPES.REMOVE_REPORTS_LIST, {
          theme: obj.themeId,
        });
      }
    },

    getReport({ commit }, obj) {
      axios.get(`/api/reports/${obj}`).then((response) => {
        commit(TYPES.SET_CURRENT_REPORT, response.data);
      }).catch((error) => {
        throw new Error(error);
      });
    },
  },
};
