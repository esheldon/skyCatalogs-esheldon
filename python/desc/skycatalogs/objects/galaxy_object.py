from .base_object import BaseObject, GALAXY, GALAXY_BULGE, GALAXY_DISK, GALAXY_KNOTS
def class GalaxyObject(BaseObject):
'''
Galaxy object.
'''
      def __init__(self, ra, dec, id, redshift=None, hp_id=None,
                   belongs_to=None, belongs_index=None)
        '''
        Minimum information needed for position static (not SSO) objects
        Type of object_type should perhaps be an enumeration
        '''
        super().__init__(ra, dec, id, BaseObject.GALAXY, redshift,
                         hp_id, belongs_to, belongs_index)

        # self._cmps = {GALAXY_BULGE : GalaxySub(self, GALAXY_BULGE),
        #               GALAXY_DISK : GalaxySub(self, GALAXY_DISK)}
        # Don't always have knots.  When we do, handling could be different
        #               GALAXY_KNOTS : GalaxySub(self, GALAXY_KNOTS)
        #    or         GALAXY_KNOTS : KnotsObject(self)

    # def get_subcomponent(self, cmp_type):
    #     return self._cmps.get(cmp_type)

    def get_flux(self, date_time, band):
        '''
        Parameters
        ----------
        date_time   datetime object; time at which flux is requested
        band        specifies interval over which flux is to be integrated
                    (and filter characteristics?)
        '''
        raise NotImplementedError

    ##### -------------------------------------------
    # Everything below this line needs thought, likely redesign

    def get_sed(self, subcomponent_list=[GALAXY_BULGE, GALAXY_DISK, GALAXY_KNOTS], **kwargs):
        '''
        For galaxies may want to specify subcomponent(s)
        '''
        d = {}
        for c in subcomponent_list:
            d[c] = self._cmps[c].get_sed(**kwargs)

        return d

    def get_sed_metadata(self, **kwargs):
        '''
        Returns, e.g,. units (wavelength or frequency) and list intervals associated
        with sed values
        '''
        d = {}
        for c in subcomponent_list:
            d[c] = self._cmps[c].get_sed_metadata(**kwargs)

        return d

# All galaxy information which is not indirected (e.g. if SEDs are stored
# in files there will be separate ones for different components) is read
# in at once. Provide a way to restrict information returned to a particular
# component if desired


def class GalaxySub(object):
    def __init__(self, parent, component_type):
        self._parent = parent
        self._cmp = component_type

    def get_sed(self):
        pass

    def

def class GalaxyKnots(object):
    def __init__(self, parent):
        self._parent = parent
        self._cmp = GALAXY_KNOTS
