#
# PySNMP MIB module BCN-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-SMI-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 15:37:39 2022
# On host fv-az135-436 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
bluecatnetworks, = mibBuilder.importSymbols("BLUECATNETWORKS-MIB", "bluecatnetworks")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, iso, IpAddress, MibIdentifier, TimeTicks, Bits, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "iso", "IpAddress", "MibIdentifier", "TimeTicks", "Bits", "Counter32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BCN-SMI-MIB", PYSNMP_MODULE_ID=bcnSMI, bcnServices=bcnServices, bcnProducts=bcnProducts, bcnSMI=bcnSMI, bcnMgmt=bcnMgmt, bcnModules=bcnModules, bcnExperimental=bcnExperimental)
