import axios from 'axios';
import * as TYPES from './types';
import helper from '../helper';

export default {
  state: {
    all: [],
    current: {},
    language: '',
    disclaimer: true,
  },

  getters: {
    getAllProjects: state => state.all,
    getCurrentProject: state => state.current,
    getDisclaimerProject: state => state.disclaimer,
    getProjectLanguages: state => state.current.languages,
    getCurrentLanguage: state => state.language,
  },

  /* eslint-disable no-param-reassign */
  mutations: {
    [TYPES.SET_PROJECTS_LIST](state, obj) {
      state.all = obj;
    },

    [TYPES.SET_CURRENT_PROJECT](state, obj) {
      state.current = obj;
      document.title = `Voices of Youth - ${obj.name}`;
    },

    [TYPES.SET_DISCLAIMER_PROJECT](state, obj) {
      state.disclaimer = obj;
    },

    [TYPES.SET_CURRENT_LANGUAGE](state, obj) {
      state.language = obj;
    },
  },

  actions: {
    setProjects({ commit }) {
      axios.get('/api/projects').then((response) => {
        commit(TYPES.SET_PROJECTS_LIST, response.data);
      }).catch((error) => {
        throw new Error(error);
      });
    },

    setCurrentProject({ commit, state }, obj) {
      if (obj) {
        commit(TYPES.SET_CURRENT_PROJECT, obj);
        localStorage.setItem('project', JSON.stringify(obj));
      } else {
        const project = JSON.parse(localStorage.getItem('project'));
        if (project) {
          commit(TYPES.SET_CURRENT_PROJECT, JSON.parse(localStorage.getItem('project')));
        } else {
          window.location = '/';
        }
      }
    },

    showDisclaimerProject({ commit }, obj) {
      commit(TYPES.SET_DISCLAIMER_PROJECT, obj);
    },

    setCurrentLanguage({ commit, state, dispatch }, obj) {
      if (obj) {
        const project = helper.getItem('project');
        axios.get(`/api/projects/${project.id}/?lang=${obj}`).then((response) => {
          localStorage.setItem('project', JSON.stringify(response.data));
          localStorage.setItem('language', JSON.stringify(obj));
          window.location.reload();
        }).catch((error) => {
          throw new Error(error);
        });
      }
    },
  },
};
