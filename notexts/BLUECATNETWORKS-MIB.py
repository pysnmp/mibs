#
# PySNMP MIB module BLUECATNETWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BLUECATNETWORKS-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 09:17:39 2023
# On host fv-az590-874 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, Gauge32, ObjectIdentity, enterprises, Bits, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter32, NotificationType, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Gauge32", "ObjectIdentity", "enterprises", "Bits", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter32", "NotificationType", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bluecatnetworksId = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 1))
bluecatnetworksId.setRevisions(('2010-11-30 00:00',))
if mibBuilder.loadTexts: bluecatnetworksId.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bluecatnetworksId.setOrganization('BlueCat Networks Inc.')
bluecatnetworks = MibIdentifier((1, 3, 6, 1, 4, 1, 13315))
appliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100))
mibBuilder.exportSymbols("BLUECATNETWORKS-MIB", PYSNMP_MODULE_ID=bluecatnetworksId, appliances=appliances, bluecatnetworksId=bluecatnetworksId, bluecatnetworks=bluecatnetworks)
