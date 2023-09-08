#
# PySNMP MIB module BEGEMOT-MIB2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-MIB2-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 07:46:12 2023
# On host fv-az268-298 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
begemotIp, = mibBuilder.importSymbols("BEGEMOT-IP-MIB", "begemotIp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, Gauge32, MibIdentifier, iso, NotificationType, ObjectIdentity, Integer32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Gauge32", "MibIdentifier", "iso", "NotificationType", "ObjectIdentity", "Integer32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
begemotMib2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1))
begemotMib2.setRevisions(('2009-08-03 00:00', '2006-02-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: begemotMib2.setRevisionsDescriptions(('Second edition adds begemotIfDataPoll object.', 'Initial revision.',))
if mibBuilder.loadTexts: begemotMib2.setLastUpdated('200908030000Z')
if mibBuilder.loadTexts: begemotMib2.setOrganization('German Aerospace Center')
if mibBuilder.loadTexts: begemotMib2.setContactInfo('\t\tHartmut Brandt\n\n\t     Postal:\tGerman Aerospace Center\n\t\t\tOberpfaffenhofen\n\t\t\t82234 Wessling\n\t\t\tGermany\n\n\t     Fax:\t+49 8153 28 2843\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: begemotMib2.setDescription('The MIB for private mib2 stuff.')
begemotIfMaxspeed = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 1), Counter64()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotIfMaxspeed.setStatus('current')
if mibBuilder.loadTexts: begemotIfMaxspeed.setDescription('The speed of the fastest interface in ifTable in bps.')
begemotIfPoll = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotIfPoll.setStatus('current')
if mibBuilder.loadTexts: begemotIfPoll.setDescription('The current polling rate for the HC 64-bit counters.')
begemotIfForcePoll = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotIfForcePoll.setStatus('current')
if mibBuilder.loadTexts: begemotIfForcePoll.setDescription('The polling rate to be enforced for the HC 64-bit counters.\n\t     If this value is 0 the mib2 module computes a polling rate\n\t     depending on the value of begemotIfMaxspeed. If this value\n\t     turns out to be wrong, the polling rate can be force to an\n\t     arbitrary value by setting begemotIfForcePoll to a non-0\n\t     value. This may be necessary if an interface announces a wrong\n\t     bit rate in its MIB.')
begemotIfDataPoll = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 4), TimeTicks().clone(100)).setUnits('deciseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotIfDataPoll.setStatus('current')
if mibBuilder.loadTexts: begemotIfDataPoll.setDescription('The rate at which the mib2 module will poll interface data.')
mibBuilder.exportSymbols("BEGEMOT-MIB2-MIB", begemotIfDataPoll=begemotIfDataPoll, begemotIfMaxspeed=begemotIfMaxspeed, begemotIfForcePoll=begemotIfForcePoll, begemotMib2=begemotMib2, PYSNMP_MODULE_ID=begemotMib2, begemotIfPoll=begemotIfPoll)
