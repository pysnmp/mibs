#
# PySNMP MIB module BCN-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-SMI-MIB
# Produced by pysmi-1.1.8 at Fri Jan 27 14:11:03 2023
# On host fv-az613-163 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
bluecatnetworks, = mibBuilder.importSymbols("BLUECATNETWORKS-MIB", "bluecatnetworks")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, Integer32, Counter64, ModuleIdentity, Bits, MibIdentifier, NotificationType, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "Integer32", "Counter64", "ModuleIdentity", "Bits", "MibIdentifier", "NotificationType", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcnSMI = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 4, 1))
bcnSMI.setRevisions(('2010-11-30 00:00',))
if mibBuilder.loadTexts: bcnSMI.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bcnSMI.setOrganization('BlueCat Networks Inc.')
bcnProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 2))
if mibBuilder.loadTexts: bcnProducts.setStatus('current')
bcnMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3))
if mibBuilder.loadTexts: bcnMgmt.setStatus('current')
bcnServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1))
if mibBuilder.loadTexts: bcnServices.setStatus('current')
bcnModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 4))
if mibBuilder.loadTexts: bcnModules.setStatus('current')
bcnExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 5))
if mibBuilder.loadTexts: bcnExperimental.setStatus('current')
mibBuilder.exportSymbols("BCN-SMI-MIB", PYSNMP_MODULE_ID=bcnSMI, bcnProducts=bcnProducts, bcnModules=bcnModules, bcnMgmt=bcnMgmt, bcnExperimental=bcnExperimental, bcnSMI=bcnSMI, bcnServices=bcnServices)
