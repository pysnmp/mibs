#
# PySNMP MIB module BCN-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-SMI-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 17:08:22 2021
# On host fv-az135-491 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
bluecatnetworks, = mibBuilder.importSymbols("BLUECATNETWORKS-MIB", "bluecatnetworks")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, Counter32, ModuleIdentity, MibIdentifier, Integer32, Bits, iso, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "Counter32", "ModuleIdentity", "MibIdentifier", "Integer32", "Bits", "iso", "NotificationType", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcnSMI = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 4, 1))
bcnSMI.setRevisions(('2010-11-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcnSMI.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bcnSMI.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bcnSMI.setOrganization('BlueCat Networks Inc.')
if mibBuilder.loadTexts: bcnSMI.setContactInfo('Adonis Technical Support\n        BlueCat Networks Inc.\n \t\t \n        Tel: +1 866 491 2228 (toll free)\n \t\t     +1 416 646 8400 (international) \n        Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bcnSMI.setDescription('The Structure of Management Information for\n        Bluecat Networks enterprise.')
bcnProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 2))
if mibBuilder.loadTexts: bcnProducts.setStatus('current')
if mibBuilder.loadTexts: bcnProducts.setDescription('bcnProducts is the root for the OID values defined in\n         BCN-PRODUCTS-MIB.\n         Products might include hardware and/or software.')
bcnMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3))
if mibBuilder.loadTexts: bcnMgmt.setStatus('current')
if mibBuilder.loadTexts: bcnMgmt.setDescription('bcnSystems is the main subtree for new MIBs.')
bcnServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1))
if mibBuilder.loadTexts: bcnServices.setStatus('current')
if mibBuilder.loadTexts: bcnServices.setDescription('bcnServices is the root for the OID values defined in \n         BCN-SERVICES-MIB.\n         The intention is that the set of services define the type of\n         system.')
bcnModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 4))
if mibBuilder.loadTexts: bcnModules.setStatus('current')
if mibBuilder.loadTexts: bcnModules.setDescription('bcnModules provides a root object identifier from which \n        MODULE-IDENTITY values may be assigned.')
bcnExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 5))
if mibBuilder.loadTexts: bcnExperimental.setStatus('current')
if mibBuilder.loadTexts: bcnExperimental.setDescription('The bcnExperimental branch is intended for work in progress mibs.\n        Objects in this part of the tree will be deleted when the work is\n        complete and moved to its permanent location.')
mibBuilder.exportSymbols("BCN-SMI-MIB", PYSNMP_MODULE_ID=bcnSMI, bcnSMI=bcnSMI, bcnExperimental=bcnExperimental, bcnModules=bcnModules, bcnServices=bcnServices, bcnProducts=bcnProducts, bcnMgmt=bcnMgmt)
