#
# PySNMP MIB module BCN-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-SMI-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:32:27 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
bluecatnetworks, = mibBuilder.importSymbols("BLUECATNETWORKS-MIB", "bluecatnetworks")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, NotificationType, Unsigned32, ObjectIdentity, TimeTicks, iso, MibIdentifier, Counter64, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Unsigned32", "ObjectIdentity", "TimeTicks", "iso", "MibIdentifier", "Counter64", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Counter32")
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
mibBuilder.exportSymbols("BCN-SMI-MIB", bcnExperimental=bcnExperimental, bcnServices=bcnServices, PYSNMP_MODULE_ID=bcnSMI, bcnMgmt=bcnMgmt, bcnProducts=bcnProducts, bcnModules=bcnModules, bcnSMI=bcnSMI)
