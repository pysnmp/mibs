#
# PySNMP MIB module BLUECATNETWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BLUECATNETWORKS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:42:04 2021
# On host fv-az36-794 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, ModuleIdentity, Integer32, ObjectIdentity, IpAddress, Bits, iso, TimeTicks, Gauge32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "ModuleIdentity", "Integer32", "ObjectIdentity", "IpAddress", "Bits", "iso", "TimeTicks", "Gauge32", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bluecatnetworksId = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 1))
bluecatnetworksId.setRevisions(('2010-11-30 00:00',))
if mibBuilder.loadTexts: bluecatnetworksId.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bluecatnetworksId.setOrganization('BlueCat Networks Inc.')
bluecatnetworks = MibIdentifier((1, 3, 6, 1, 4, 1, 13315))
appliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100))
mibBuilder.exportSymbols("BLUECATNETWORKS-MIB", bluecatnetworks=bluecatnetworks, appliances=appliances, bluecatnetworksId=bluecatnetworksId, PYSNMP_MODULE_ID=bluecatnetworksId)
